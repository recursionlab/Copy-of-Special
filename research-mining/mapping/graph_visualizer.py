"""
Graph Visualization Module - creates interactive and static visualizations of concept networks.

Features:
- Interactive plotly visualizations
- Static matplotlib plots
- Network layout algorithms
- Cluster highlighting
- Export capabilities
"""

from typing import Dict, List, Set, Tuple, Any, Optional
import json
import networkx as nx
import numpy as np

# Optional imports with fallbacks
try:
    import matplotlib.pyplot as plt
    import matplotlib.patches as patches
    MATPLOTLIB_AVAILABLE = True
except ImportError:
    MATPLOTLIB_AVAILABLE = False

try:
    import plotly.graph_objects as go
    import plotly.express as px
    from plotly.offline import plot
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False


class GraphVisualizer:
    """Creates visualizations of concept network graphs."""

    def __init__(self, concept_mapper):
        self.concept_mapper = concept_mapper
        self.concept_graph = concept_mapper.concept_graph
        self.document_graph = concept_mapper.document_graph
        self.cluster_graph = concept_mapper.cluster_graph

    def create_interactive_concept_graph(self, output_path: str, max_nodes: int = 500) -> bool:
        """Create interactive Plotly visualization of concept graph."""
        if not PLOTLY_AVAILABLE:
            print("Plotly not available - install with: pip install plotly")
            return False

        # Limit nodes for performance
        if self.concept_graph.number_of_nodes() > max_nodes:
            # Get most connected nodes
            degrees = dict(self.concept_graph.degree())
            top_nodes = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:max_nodes]
            node_ids = [node for node, _ in top_nodes]
            subgraph = self.concept_graph.subgraph(node_ids)
        else:
            subgraph = self.concept_graph

        # Calculate layout
        pos = nx.spring_layout(subgraph, k=1, iterations=50)

        # Prepare node data
        node_x, node_y = [], []
        node_text, node_info = [], []
        node_colors = []

        # Color mapping for types
        types = list(set(subgraph.nodes[node].get('type', 'unknown') for node in subgraph.nodes()))
        color_map = {t: px.colors.qualitative.Set3[i % len(px.colors.qualitative.Set3)]
                     for i, t in enumerate(types)}

        for node in subgraph.nodes():
            x, y = pos[node]
            node_x.append(x)
            node_y.append(y)

            node_data = subgraph.nodes[node]
            node_type = node_data.get('type', 'unknown')
            definition = node_data.get('definition', '')
            confidence = node_data.get('confidence', 0.5)

            node_text.append(f"{node}<br>Type: {node_type}")
            node_info.append(f"ID: {node}<br>Type: {node_type}<br>Confidence: {confidence:.2f}<br>Definition: {definition[:100]}...")
            node_colors.append(color_map[node_type])

        # Prepare edge data
        edge_x, edge_y = [], []
        for edge in subgraph.edges():
            x0, y0 = pos[edge[0]]
            x1, y1 = pos[edge[1]]
            edge_x.extend([x0, x1, None])
            edge_y.extend([y0, y1, None])

        # Create edge trace
        edge_trace = go.Scatter(
            x=edge_x, y=edge_y,
            line=dict(width=0.5, color='#888'),
            hoverinfo='none',
            mode='lines'
        )

        # Create node trace
        node_trace = go.Scatter(
            x=node_x, y=node_y,
            mode='markers+text',
            hoverinfo='text',
            text=node_text,
            hovertext=node_info,
            textposition="middle center",
            marker=dict(
                size=10,
                color=node_colors,
                line=dict(width=2, color='black')
            )
        )

        # Create figure
        fig = go.Figure(
            data=[edge_trace, node_trace],
            layout=go.Layout(
                title='Concept Network Graph',
                titlefont_size=16,
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                annotations=[
                    dict(
                        text="Concept relationships and clusters",
                        showarrow=False,
                        xref="paper", yref="paper",
                        x=0.005, y=-0.002,
                        xanchor="left", yanchor="bottom",
                        font=dict(color="black", size=12)
                    )
                ],
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
            )
        )

        # Save to file
        plot(fig, filename=output_path, auto_open=False)
        return True

    def create_static_concept_graph(self, output_path: str, max_nodes: int = 200) -> bool:
        """Create static matplotlib visualization of concept graph."""
        if not MATPLOTLIB_AVAILABLE:
            print("Matplotlib not available - install with: pip install matplotlib")
            return False

        # Limit nodes for clarity
        if self.concept_graph.number_of_nodes() > max_nodes:
            degrees = dict(self.concept_graph.degree())
            top_nodes = sorted(degrees.items(), key=lambda x: x[1], reverse=True)[:max_nodes]
            node_ids = [node for node, _ in top_nodes]
            subgraph = self.concept_graph.subgraph(node_ids)
        else:
            subgraph = self.concept_graph

        # Calculate layout
        pos = nx.spring_layout(subgraph, k=2, iterations=50)

        # Set up colors by type
        types = list(set(subgraph.nodes[node].get('type', 'unknown') for node in subgraph.nodes()))
        colors = plt.cm.Set3(np.linspace(0, 1, len(types)))
        type_to_color = {t: colors[i] for i, t in enumerate(types)}

        node_colors = [type_to_color[subgraph.nodes[node].get('type', 'unknown')] for node in subgraph.nodes()]

        # Create plot
        plt.figure(figsize=(16, 12))

        # Draw edges
        nx.draw_networkx_edges(subgraph, pos, alpha=0.3, width=0.5, edge_color='gray')

        # Draw nodes
        nx.draw_networkx_nodes(
            subgraph, pos,
            node_color=node_colors,
            node_size=300,
            alpha=0.8
        )

        # Draw labels for high-degree nodes only
        high_degree_nodes = [node for node, degree in subgraph.degree() if degree > 2]
        labels = {node: node.split('-')[0][:10] for node in high_degree_nodes}  # Shorten labels
        nx.draw_networkx_labels(subgraph, pos, labels, font_size=8)

        # Create legend
        legend_elements = [patches.Patch(color=type_to_color[t], label=t) for t in types[:10]]  # Limit legend size
        plt.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.15, 1))

        plt.title('Concept Network Graph', size=16)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return True

    def create_cluster_visualization(self, clusters: List[List[int]], output_path: str) -> bool:
        """Create visualization highlighting concept clusters."""
        if not MATPLOTLIB_AVAILABLE:
            return False

        # Build cluster graph
        cluster_graph = self.concept_mapper.build_cluster_relationship_graph(clusters)

        if cluster_graph.number_of_nodes() == 0:
            return False

        # Calculate layout
        pos = nx.spring_layout(cluster_graph, k=3, iterations=50)

        # Create plot
        plt.figure(figsize=(14, 10))

        # Draw edges with weights
        edges = cluster_graph.edges(data=True)
        for edge in edges:
            x1, y1 = pos[edge[0]]
            x2, y2 = pos[edge[1]]
            weight = edge[2].get('weight', 1)
            plt.plot([x1, x2], [y1, y2], 'k-', alpha=0.3, linewidth=weight/2)

        # Draw nodes with sizes based on cluster size
        node_sizes = [cluster_graph.nodes[node].get('size', 10) * 50 for node in cluster_graph.nodes()]
        node_colors = plt.cm.viridis(np.linspace(0, 1, cluster_graph.number_of_nodes()))

        nx.draw_networkx_nodes(
            cluster_graph, pos,
            node_size=node_sizes,
            node_color=node_colors,
            alpha=0.7
        )

        # Add labels with cluster info
        labels = {}
        for node in cluster_graph.nodes():
            size = cluster_graph.nodes[node].get('size', 0)
            types = cluster_graph.nodes[node].get('types', [])
            main_type = types[0] if types else 'unknown'
            labels[node] = f"C{node}\n{size} concepts\n{main_type}"

        nx.draw_networkx_labels(cluster_graph, pos, labels, font_size=8)

        plt.title('Concept Cluster Relationships', size=16)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return True

    def create_document_network(self, output_path: str) -> bool:
        """Create visualization of document relationships."""
        if not MATPLOTLIB_AVAILABLE:
            return False

        # Build document graph
        doc_graph = self.concept_mapper.build_document_dependency_graph()

        if doc_graph.number_of_nodes() == 0:
            return False

        # Calculate layout
        pos = nx.spring_layout(doc_graph, k=2, iterations=50)

        # Create plot
        plt.figure(figsize=(16, 12))

        # Draw edges with weights based on similarity
        for edge in doc_graph.edges(data=True):
            x1, y1 = pos[edge[0]]
            x2, y2 = pos[edge[1]]
            similarity = edge[2].get('jaccard_similarity', 0)
            plt.plot([x1, x2], [y1, y2], 'b-', alpha=similarity, linewidth=similarity*3)

        # Draw nodes with sizes based on concept count
        node_sizes = [doc_graph.nodes[node].get('concept_count', 10) * 10 for node in doc_graph.nodes()]

        nx.draw_networkx_nodes(
            doc_graph, pos,
            node_size=node_sizes,
            node_color='lightblue',
            alpha=0.8
        )

        # Add document name labels (shortened)
        labels = {}
        for node in doc_graph.nodes():
            # Extract filename from path
            doc_name = node.split('/')[-1].split('\\')[-1]
            if len(doc_name) > 20:
                doc_name = doc_name[:20] + '...'
            concept_count = doc_graph.nodes[node].get('concept_count', 0)
            labels[node] = f"{doc_name}\n({concept_count} concepts)"

        nx.draw_networkx_labels(doc_graph, pos, labels, font_size=6)

        plt.title('Document Relationship Network', size=16)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return True

    def create_type_relationship_graph(self, output_path: str) -> bool:
        """Create visualization of concept type relationships."""
        if not MATPLOTLIB_AVAILABLE:
            return False

        # Build type graph
        type_graph = self.concept_mapper.build_concept_type_graph()

        if type_graph.number_of_nodes() == 0:
            return False

        # Calculate layout
        pos = nx.spring_layout(type_graph, k=3, iterations=50)

        # Create plot
        plt.figure(figsize=(12, 10))

        # Draw edges with weights
        for edge in type_graph.edges(data=True):
            x1, y1 = pos[edge[0]]
            x2, y2 = pos[edge[1]]
            weight = edge[2].get('weight', 0.1)
            plt.plot([x1, x2], [y1, y2], 'g-', alpha=weight*2, linewidth=weight*5)

        # Draw nodes with sizes based on concept count
        node_sizes = [type_graph.nodes[node].get('concept_count', 1) * 20 for node in type_graph.nodes()]

        nx.draw_networkx_nodes(
            type_graph, pos,
            node_size=node_sizes,
            node_color='lightgreen',
            alpha=0.8
        )

        # Add type labels
        labels = {}
        for node in type_graph.nodes():
            count = type_graph.nodes[node].get('concept_count', 0)
            labels[node] = f"{node}\n({count})"

        nx.draw_networkx_labels(type_graph, pos, labels, font_size=10)

        plt.title('Concept Type Relationships', size=16)
        plt.axis('off')
        plt.tight_layout()
        plt.savefig(output_path, dpi=300, bbox_inches='tight')
        plt.close()
        return True

    def export_all_visualizations(self, output_dir: str, clusters: Optional[List[List[int]]] = None) -> Dict[str, bool]:
        """Export all available visualizations."""
        import os
        os.makedirs(output_dir, exist_ok=True)

        results = {}

        # Interactive concept graph
        if PLOTLY_AVAILABLE:
            results['interactive_concept_graph'] = self.create_interactive_concept_graph(
                f"{output_dir}/interactive_concept_graph.html"
            )
        else:
            results['interactive_concept_graph'] = False

        # Static visualizations
        if MATPLOTLIB_AVAILABLE:
            results['static_concept_graph'] = self.create_static_concept_graph(
                f"{output_dir}/concept_graph.png"
            )
            results['document_network'] = self.create_document_network(
                f"{output_dir}/document_network.png"
            )
            results['type_relationship_graph'] = self.create_type_relationship_graph(
                f"{output_dir}/type_relationships.png"
            )

            if clusters:
                results['cluster_visualization'] = self.create_cluster_visualization(
                    clusters, f"{output_dir}/cluster_relationships.png"
                )
        else:
            results.update({
                'static_concept_graph': False,
                'document_network': False,
                'type_relationship_graph': False,
                'cluster_visualization': False
            })

        return results