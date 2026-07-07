"""
Concept Mapping Module - generates NetworkX graphs of concept relationships and document dependencies.

Creates:
- Concept relationship graphs
- Document-to-concept dependency graphs
- Cluster relationship networks
- Cross-reference graphs
"""

from typing import Dict, List, Set, Tuple, Any, Optional
import json
from collections import defaultdict, Counter
import networkx as nx
import numpy as np


class ConceptMapper:
    """Maps ConceptUnits into network graphs for analysis and visualization."""

    def __init__(self, units: List[Dict[str, Any]]):
        self.units = units
        self.id_to_unit = {u['id']: u for u in units}
        self.concept_graph = nx.MultiDiGraph()
        self.document_graph = nx.Graph()
        self.cluster_graph = nx.Graph()
        self._build_base_graphs()

    def _build_base_graphs(self) -> None:
        """Build the foundational graphs from ConceptUnits."""
        # Add all concepts as nodes
        for unit in self.units:
            self.concept_graph.add_node(
                unit['id'],
                type=unit.get('type', 'unknown'),
                definition=unit.get('definition', ''),
                confidence=unit.get('confidence_score', 0.5),
                source=unit.get('source', ''),
                tags=unit.get('tags', [])
            )

        # Add relationships as edges
        for unit in self.units:
            unit_id = unit['id']
            relations = unit.get('relations', [])

            for relation in relations:
                if isinstance(relation, dict):
                    target_id = relation.get('id') or relation.get('concept_id')
                    relation_type = relation.get('type', 'related_to')

                    if target_id and target_id in self.id_to_unit:
                        self.concept_graph.add_edge(
                            unit_id,
                            target_id,
                            relation_type=relation_type,
                            weight=1.0
                        )
                elif isinstance(relation, str) and relation in self.id_to_unit:
                    self.concept_graph.add_edge(
                        unit_id,
                        relation,
                        relation_type='related_to',
                        weight=1.0
                    )

    def build_document_dependency_graph(self) -> nx.Graph:
        """Create graph showing relationships between documents based on shared concepts."""
        # Group concepts by source document
        doc_concepts = defaultdict(set)
        for unit in self.units:
            source = unit.get('source', 'unknown')
            doc_concepts[source].add(unit['id'])

        # Create document nodes
        for doc in doc_concepts:
            self.document_graph.add_node(doc, concept_count=len(doc_concepts[doc]))

        # Add edges between documents that share concepts
        docs = list(doc_concepts.keys())
        for i, doc1 in enumerate(docs):
            for doc2 in docs[i + 1:]:
                shared_concepts = doc_concepts[doc1] & doc_concepts[doc2]
                if shared_concepts:
                    # Calculate Jaccard similarity
                    jaccard = len(shared_concepts) / len(doc_concepts[doc1] | doc_concepts[doc2])
                    self.document_graph.add_edge(
                        doc1,
                        doc2,
                        shared_concepts=len(shared_concepts),
                        jaccard_similarity=jaccard,
                        weight=jaccard
                    )

        return self.document_graph

    def build_concept_type_graph(self) -> nx.Graph:
        """Create graph showing relationships between concept types."""
        type_graph = nx.Graph()

        # Count concepts by type
        type_counts = Counter(unit.get('type', 'unknown') for unit in self.units)

        # Add type nodes
        for concept_type, count in type_counts.items():
            type_graph.add_node(concept_type, concept_count=count)

        # Add edges between types that share relationships
        type_relations = defaultdict(lambda: defaultdict(int))

        for unit in self.units:
            unit_type = unit.get('type', 'unknown')
            relations = unit.get('relations', [])

            for relation in relations:
                target_id = None
                if isinstance(relation, dict):
                    target_id = relation.get('id') or relation.get('concept_id')
                elif isinstance(relation, str):
                    target_id = relation

                if target_id and target_id in self.id_to_unit:
                    target_type = self.id_to_unit[target_id].get('type', 'unknown')
                    if unit_type != target_type:
                        type_relations[unit_type][target_type] += 1

        # Add weighted edges between types
        for from_type, targets in type_relations.items():
            for to_type, count in targets.items():
                if count > 0:  # Threshold for meaningful connections
                    weight = count / max(type_counts[from_type], type_counts[to_type])
                    type_graph.add_edge(from_type, to_type, weight=weight, relation_count=count)

        return type_graph

    def build_cluster_relationship_graph(self, clusters: List[List[int]]) -> nx.Graph:
        """Create graph showing relationships between concept clusters."""
        # Map unit indices to cluster IDs
        unit_to_cluster = {}
        for cluster_id, cluster_indices in enumerate(clusters):
            for unit_idx in cluster_indices:
                if unit_idx < len(self.units):
                    unit_to_cluster[self.units[unit_idx]['id']] = cluster_id

        # Add cluster nodes
        for cluster_id, cluster_indices in enumerate(clusters):
            cluster_units = [self.units[i] for i in cluster_indices if i < len(self.units)]
            cluster_types = [u.get('type', 'unknown') for u in cluster_units]
            avg_confidence = sum(u.get('confidence_score', 0.5) for u in cluster_units) / len(cluster_units)

            self.cluster_graph.add_node(
                cluster_id,
                size=len(cluster_units),
                types=list(set(cluster_types)),
                avg_confidence=avg_confidence
            )

        # Add edges between clusters based on inter-cluster relationships
        cluster_connections = defaultdict(lambda: defaultdict(int))

        for unit in self.units:
            unit_id = unit['id']
            if unit_id not in unit_to_cluster:
                continue

            unit_cluster = unit_to_cluster[unit_id]
            relations = unit.get('relations', [])

            for relation in relations:
                target_id = None
                if isinstance(relation, dict):
                    target_id = relation.get('id') or relation.get('concept_id')
                elif isinstance(relation, str):
                    target_id = relation

                if target_id and target_id in unit_to_cluster:
                    target_cluster = unit_to_cluster[target_id]
                    if unit_cluster != target_cluster:
                        cluster_connections[unit_cluster][target_cluster] += 1

        # Add weighted edges between clusters
        for from_cluster, targets in cluster_connections.items():
            for to_cluster, count in targets.items():
                if count > 0:
                    self.cluster_graph.add_edge(
                        from_cluster,
                        to_cluster,
                        weight=count,
                        connection_strength=count
                    )

        return self.cluster_graph

    def analyze_network_properties(self) -> Dict[str, Any]:
        """Analyze structural properties of the concept network."""
        properties = {}

        # Basic graph metrics
        properties['basic_metrics'] = {
            'num_nodes': self.concept_graph.number_of_nodes(),
            'num_edges': self.concept_graph.number_of_edges(),
            'density': nx.density(self.concept_graph),
            'is_connected': nx.is_weakly_connected(self.concept_graph)
        }

        # Convert to undirected for certain metrics
        undirected = self.concept_graph.to_undirected()

        if undirected.number_of_nodes() > 0:
            # Centrality measures
            properties['centrality'] = {
                'degree_centrality': dict(nx.degree_centrality(undirected)),
                'betweenness_centrality': dict(nx.betweenness_centrality(undirected, k=min(100, undirected.number_of_nodes()))),
                'closeness_centrality': dict(nx.closeness_centrality(undirected))
            }

            # Community detection
            try:
                communities = list(nx.community.greedy_modularity_communities(undirected))
                properties['communities'] = {
                    'num_communities': len(communities),
                    'modularity': nx.community.modularity(undirected, communities),
                    'community_sizes': [len(c) for c in communities]
                }
            except:
                properties['communities'] = {'error': 'Community detection failed'}

            # Network structure
            if nx.is_connected(undirected):
                properties['structure'] = {
                    'diameter': nx.diameter(undirected),
                    'average_shortest_path_length': nx.average_shortest_path_length(undirected),
                    'radius': nx.radius(undirected)
                }
            else:
                # For disconnected graphs, analyze largest component
                largest_cc = max(nx.connected_components(undirected), key=len)
                largest_subgraph = undirected.subgraph(largest_cc)
                properties['structure'] = {
                    'num_connected_components': nx.number_connected_components(undirected),
                    'largest_component_size': len(largest_cc),
                    'largest_component_diameter': nx.diameter(largest_subgraph) if len(largest_cc) > 1 else 0
                }

        return properties

    def find_concept_bridges(self, threshold: float = 0.1) -> List[Dict[str, Any]]:
        """Find concepts that act as bridges between different parts of the network."""
        undirected = self.concept_graph.to_undirected()
        bridges = []

        if undirected.number_of_nodes() < 2:
            return bridges

        # Calculate betweenness centrality
        betweenness = nx.betweenness_centrality(undirected)

        # Find high-betweenness nodes (potential bridges)
        for node_id, centrality in betweenness.items():
            if centrality > threshold:
                unit = self.id_to_unit[node_id]
                bridges.append({
                    'concept_id': node_id,
                    'type': unit.get('type', 'unknown'),
                    'betweenness_centrality': centrality,
                    'degree': undirected.degree(node_id),
                    'definition': unit.get('definition', '')[:200] + '...' if len(unit.get('definition', '')) > 200 else unit.get('definition', ''),
                    'bridge_type': 'high_betweenness'
                })

        # Find articulation points (removal disconnects graph)
        try:
            articulation_points = list(nx.articulation_points(undirected))
            for node_id in articulation_points:
                if node_id not in [b['concept_id'] for b in bridges]:  # Avoid duplicates
                    unit = self.id_to_unit[node_id]
                    bridges.append({
                        'concept_id': node_id,
                        'type': unit.get('type', 'unknown'),
                        'betweenness_centrality': betweenness.get(node_id, 0),
                        'degree': undirected.degree(node_id),
                        'definition': unit.get('definition', '')[:200] + '...' if len(unit.get('definition', '')) > 200 else unit.get('definition', ''),
                        'bridge_type': 'articulation_point'
                    })
        except:
            pass  # Graph might not support articulation points

        return sorted(bridges, key=lambda x: x['betweenness_centrality'], reverse=True)

    def export_graphs(self, output_dir: str) -> None:
        """Export graphs in multiple formats."""
        import os
        os.makedirs(output_dir, exist_ok=True)

        # Export concept graph
        nx.write_gexf(self.concept_graph, f"{output_dir}/concept_graph.gexf")
        nx.write_graphml(self.concept_graph, f"{output_dir}/concept_graph.graphml")

        # Export document graph if built
        if self.document_graph.number_of_nodes() > 0:
            nx.write_gexf(self.document_graph, f"{output_dir}/document_graph.gexf")
            nx.write_graphml(self.document_graph, f"{output_dir}/document_graph.graphml")

        # Export cluster graph if built
        if self.cluster_graph.number_of_nodes() > 0:
            nx.write_gexf(self.cluster_graph, f"{output_dir}/cluster_graph.gexf")
            nx.write_graphml(self.cluster_graph, f"{output_dir}/cluster_graph.graphml")

        # Export network analysis
        network_props = self.analyze_network_properties()
        bridges = self.find_concept_bridges()

        analysis_report = {
            'network_properties': network_props,
            'concept_bridges': bridges,
            'export_info': {
                'concept_graph_nodes': self.concept_graph.number_of_nodes(),
                'concept_graph_edges': self.concept_graph.number_of_edges(),
                'document_graph_nodes': self.document_graph.number_of_nodes(),
                'cluster_graph_nodes': self.cluster_graph.number_of_nodes()
            }
        }

        with open(f"{output_dir}/network_analysis.json", 'w', encoding='utf-8') as f:
            json.dump(analysis_report, f, ensure_ascii=False, indent=2)