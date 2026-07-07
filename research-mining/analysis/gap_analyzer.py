"""
Gap Analysis Engine for detecting missing concept relationships and orphaned concepts.

Identifies:
- Orphaned concepts without relations
- Missing bidirectional relationships
- Incomplete concept definitions
- Potential concept bridges based on semantic similarity
"""

from typing import Dict, List, Set, Tuple, Any
import json
from collections import defaultdict
import re


class GapAnalyzer:
    """Analyzes ConceptUnit collections for gaps and missing relationships."""

    def __init__(self, units: List[Dict[str, Any]]):
        self.units = units
        self.id_to_unit = {u['id']: u for u in units}
        self.relation_graph = self._build_relation_graph()

    def _build_relation_graph(self) -> Dict[str, Set[str]]:
        """Build bidirectional relation graph from units."""
        graph = defaultdict(set)

        for unit in self.units:
            unit_id = unit['id']
            relations = unit.get('relations', [])

            for relation in relations:
                if isinstance(relation, dict):
                    related_id = relation.get('id') or relation.get('concept_id')
                    if related_id:
                        graph[unit_id].add(related_id)
                        graph[related_id].add(unit_id)  # bidirectional
                elif isinstance(relation, str):
                    graph[unit_id].add(relation)
                    graph[relation].add(unit_id)

        return graph

    def find_orphaned_concepts(self) -> List[Dict[str, Any]]:
        """Find concepts with no relationships to other concepts."""
        orphaned = []

        for unit in self.units:
            unit_id = unit['id']
            relations = unit.get('relations', [])

            # Check if has meaningful relations
            has_relations = bool(relations) and any(
                isinstance(r, dict) and (r.get('id') or r.get('concept_id'))
                or isinstance(r, str) and r in self.id_to_unit
                for r in relations
            )

            if not has_relations:
                orphaned.append({
                    'id': unit_id,
                    'type': unit.get('type'),
                    'definition': unit.get('definition', '')[:200] + '...' if len(unit.get('definition', '')) > 200 else unit.get('definition', ''),
                    'confidence_score': unit.get('confidence_score'),
                    'gap_type': 'orphaned_concept'
                })

        return orphaned

    def find_missing_bidirectional_relations(self) -> List[Dict[str, Any]]:
        """Find concepts that reference others but aren't referenced back."""
        missing_bidir = []

        for unit in self.units:
            unit_id = unit['id']
            relations = unit.get('relations', [])

            for relation in relations:
                related_id = None
                if isinstance(relation, dict):
                    related_id = relation.get('id') or relation.get('concept_id')
                elif isinstance(relation, str):
                    related_id = relation

                if related_id and related_id in self.id_to_unit:
                    # Check if the related concept references back
                    related_unit = self.id_to_unit[related_id]
                    related_relations = related_unit.get('relations', [])

                    references_back = any(
                        (isinstance(r, dict) and (r.get('id') == unit_id or r.get('concept_id') == unit_id))
                        or (isinstance(r, str) and r == unit_id)
                        for r in related_relations
                    )

                    if not references_back:
                        missing_bidir.append({
                            'from_id': unit_id,
                            'to_id': related_id,
                            'from_type': unit.get('type'),
                            'to_type': related_unit.get('type'),
                            'gap_type': 'missing_bidirectional_relation',
                            'confidence_score': min(
                                unit.get('confidence_score', 0.5),
                                related_unit.get('confidence_score', 0.5)
                            )
                        })

        return missing_bidir

    def find_incomplete_definitions(self) -> List[Dict[str, Any]]:
        """Find concepts with incomplete or very short definitions."""
        incomplete = []

        for unit in self.units:
            definition = unit.get('definition', '').strip()

            # Check for incomplete definition indicators
            is_incomplete = (
                len(definition) < 20 or  # Very short
                definition.lower().endswith(('...', 'etc', 'and so on')) or  # Truncated
                re.search(r'\b(undefined|unclear|unknown|partial)\b', definition.lower()) or  # Explicit markers
                definition.count(' ') < 3  # Too few words
            )

            if is_incomplete:
                incomplete.append({
                    'id': unit['id'],
                    'type': unit.get('type'),
                    'definition': definition,
                    'definition_length': len(definition),
                    'gap_type': 'incomplete_definition',
                    'confidence_score': unit.get('confidence_score')
                })

        return incomplete

    def find_isolated_clusters(self) -> List[Dict[str, Any]]:
        """Find clusters of concepts that are disconnected from the main graph."""
        visited = set()
        clusters = []

        def dfs(node_id: str, cluster: Set[str]):
            if node_id in visited or node_id not in self.id_to_unit:
                return
            visited.add(node_id)
            cluster.add(node_id)

            for neighbor in self.relation_graph.get(node_id, []):
                dfs(neighbor, cluster)

        # Find all connected components
        for unit in self.units:
            unit_id = unit['id']
            if unit_id not in visited:
                cluster = set()
                dfs(unit_id, cluster)
                if cluster:
                    clusters.append(cluster)

        # Sort by size, largest first
        clusters.sort(key=len, reverse=True)

        isolated_clusters = []
        if len(clusters) > 1:  # More than one component means isolation
            for i, cluster in enumerate(clusters[1:], 1):  # Skip the largest
                cluster_units = [self.id_to_unit[uid] for uid in cluster if uid in self.id_to_unit]
                isolated_clusters.append({
                    'cluster_id': i,
                    'size': len(cluster),
                    'concept_ids': list(cluster),
                    'concept_types': [u.get('type') for u in cluster_units],
                    'gap_type': 'isolated_cluster',
                    'avg_confidence': sum(u.get('confidence_score', 0.5) for u in cluster_units) / len(cluster_units) if cluster_units else 0
                })

        return isolated_clusters

    def analyze_all_gaps(self) -> Dict[str, List[Dict[str, Any]]]:
        """Run all gap analysis methods and return comprehensive results."""
        return {
            'orphaned_concepts': self.find_orphaned_concepts(),
            'missing_bidirectional_relations': self.find_missing_bidirectional_relations(),
            'incomplete_definitions': self.find_incomplete_definitions(),
            'isolated_clusters': self.find_isolated_clusters()
        }

    def export_gap_report(self, output_path: str) -> None:
        """Export gap analysis results to JSON file."""
        gaps = self.analyze_all_gaps()

        # Add summary statistics
        report = {
            'metadata': {
                'total_concepts': len(self.units),
                'total_gaps_found': sum(len(gap_list) for gap_list in gaps.values()),
                'analysis_date': json.dumps({}),  # Will be filled with actual timestamp
                'gap_types': list(gaps.keys())
            },
            'summary': {
                gap_type: len(gap_list) for gap_type, gap_list in gaps.items()
            },
            'gaps': gaps
        }

        import datetime
        report['metadata']['analysis_date'] = datetime.datetime.now().isoformat()

        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=2)