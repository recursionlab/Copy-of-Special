import numpy as np
import gudhi as gd
import pulp
from itertools import combinations
from halira_kernel.utils.env import HAS_SAGE

class CohomologyGeneratorExtractor:
    def __init__(self, X, max_edge_length=0.25, max_dim=2, prime=2):
        self.X = np.array(X)
        self.max_edge_length = max_edge_length
        self.max_dim = max_dim
        self.prime = prime
        self.st = None
        self.edges = None
        self.edge_idx = None

    def build_rips(self):
        rips = gd.RipsComplex(points=self.X, max_edge_length=self.max_edge_length)
        self.st = rips.create_simplex_tree(max_dimension=self.max_dim)
        self.st.compute_persistence()
        return self.st

    def extract_cocycles(self, min_persistence=0.0):
        if self.st is None:
            self.build_rips()

        if not hasattr(self.st, 'compute_persistence'):
             # Check if gudhi tree was properly initialized
             return []

        # Gudhi's cohomology_generators_in_dimension expects persistence to be computed
        # with persistence_dim_max=True for cocycles
        self.st.compute_persistence(persistence_dim_max=True)
        cocycles = self.st.cohomology_generators_in_dimension(1, prime=self.prime)

        filtered = []
        for (birth, death), cocycle_map in cocycles:
            persistence = death - birth if death < np.inf else np.inf
            if persistence >= min_persistence:
                # cocycle_map is a dict mapping (vertex_i, vertex_j) to coefficient
                filtered.append((birth, death, cocycle_map))
        return filtered

    def build_edge_graph(self):
        n = len(self.X)
        edges = []
        edge_idx = {}
        for i, j in combinations(range(n), 2):
            dist = np.linalg.norm(self.X[i] - self.X[j])
            if dist <= self.max_edge_length:
                k = len(edges)
                edges.append((i, j, dist))
                edge_idx[(i, j)] = k
                edge_idx[(j, i)] = k # For undirected graph
        self.edges = edges
        self.edge_idx = edge_idx
        return edges, edge_idx

    def cocycle_to_minimal_cycle(self, cocycle_map):
        if self.edges is None or self.edge_idx is None:
            self.build_edge_graph()

        edges = self.edges
        edge_idx = self.edge_idx
        n_points = len(self.X)

        prob = pulp.LpProblem("minimal_cycle", pulp.LpMinimize)

        # Binary variables for each edge (x_k = 1 if edge k is in cycle, 0 otherwise)
        x = [pulp.LpVariable(f"x_{k}", cat="Binary") for k in range(len(edges))]

        # Objective: minimize total edge length (or number of edges for minimal support)
        # For minimal length, use edge_list[k][2] (the distance)
        # For minimal support, use 1 (count edges)
        prob += pulp.lpSum(edges[k][2] * x[k] for k in range(len(edges))) # Minimal length

        # Constraint 1: Every vertex in the cycle must have an even degree (mod 2)
        # This ensures it's a cycle
        for v in range(n_points):
            incident_edges_indices = [k for k, (i, j, _) in enumerate(edges) if i == v or j == v]
            prob += pulp.lpSum(x[k] for k in incident_edges_indices) % 2 == 0

        # Constraint 2: Cocycle pairing constraint
        # The sum of cocycle coefficients * x_k must be 1 (mod prime)
        # This ensures the cycle is a generator for the given cocycle
        cocycle_sum_expr = []
        for (u, v), coeff in cocycle_map.items():
            if (u, v) in edge_idx: # Ensure edge exists in our graph
                cocycle_sum_expr.append(coeff * x[edge_idx[(u, v)]])
            elif (v, u) in edge_idx: # Check reverse direction for undirected edges
                cocycle_sum_expr.append(coeff * x[edge_idx[(v, u)]])
        
        # For prime=2, this is a parity constraint
        if self.prime == 2:
            prob += pulp.lpSum(cocycle_sum_expr) % 2 == 1
        else:
            # For other primes, this is more complex and requires integer programming
            # For simplicity, we'll stick to prime=2 for now for minimal cycles
            raise NotImplementedError("Minimal cycle extraction for prime > 2 not implemented.")

        prob.solve(pulp.PULP_CBC_CMD(msg=False))

        if prob.status != pulp.LpStatusOptimal:
            return [] # No optimal solution found

        cycle_edges = [edges[k] for k in range(len(edges)) if pulp.value(x[k]) == 1]
        return cycle_edges

    def edges_to_loop(self, cycle_edges):
        """
        Convert a list of edges forming a cycle into an ordered loop of vertices.
        """
        if not cycle_edges:
            return []

        adj = {}
        for u, v, _ in cycle_edges:
            adj.setdefault(u, []).append(v)
            adj.setdefault(v, []).append(u)

        # Find a starting point with degree 2 (must be a simple cycle)
        start_node = -1
        for node, neighbors in adj.items():
            if len(neighbors) == 2: # Simple cycle
                start_node = node
                break
        if start_node == -1: # Fallback if not a simple cycle (e.g., multiple components)
            start_node = cycle_edges[0][0]

        loop = [start_node]
        prev_node = None
        curr_node = start_node

        while True:
            neighbors = adj.get(curr_node, [])
            next_node = None
            for neighbor in neighbors:
                if neighbor != prev_node:
                    next_node = neighbor
                    break
            
            if next_node is None: # Dead end or isolated node
                break
            
            if next_node == start_node and len(loop) > 1: # Loop closed
                loop.append(start_node)
                break
            
            if next_node in loop: # Cycle detected but not closed to start_node
                # This can happen if the LP solution is not a simple cycle
                # For now, break to avoid infinite loop, but indicates complex topology
                break

            loop.append(next_node)
            prev_node = curr_node
            curr_node = next_node
            
            if len(loop) > len(self.X) * 2: # Safety break for very long paths
                break

        return loop

    def get_generators(self, min_persistence=0.0, metric="length"):
        """
        Full pipeline to extract H1 generators as minimal cycles.
        metric: "length" (shortest geometric loop) or "support" (fewest edges)
        """
        cocycles = self.extract_cocycles(min_persistence=min_persistence)
        generators = []
        for birth, death, cocycle_map in cocycles:
            # Modify objective in cocycle_to_minimal_cycle based on metric
            # For now, it's hardcoded to length (edge_list[k][2])
            # To change to support, replace edge_list[k][2] with 1
            cycle_edges = self.cocycle_to_minimal_cycle(cocycle_map)
            loop = self.edges_to_loop(cycle_edges)
            generators.append({
                "birth": birth,
                "death": death,
                "edges": cycle_edges,
                "loop": loop,
                "cocycle_map": cocycle_map # Include cocycle map for reference
            })
        return generators