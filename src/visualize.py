from collections import defaultdict
from typing import Dict, List, Tuple
import matplotlib.pyplot as plt
import networkx as nx


def build_nx_graph(edges: List[Tuple[str, str]]) -> nx.Graph:
    """Constructs an undirected NetworkX graph with aggregated edge weights."""
    g = nx.Graph()
    edge_counts: Dict[Tuple[str, str], int] = defaultdict(int)

    for u, v in edges:
        normalized_edge = (u, v) if u <= v else (v, u)
        edge_counts[normalized_edge] += 1

    for (u, v), weight in edge_counts.items():
        g.add_edge(u, v, weight=weight)
    return g


def plot_benchmark_results(results: List[Dict]):
    """Plots comparative execution runtimes for DFS vs BFS."""
    labels = [r["dataset"] for r in results]
    dfs_times = [r["dfs_time"] for r in results]
    bfs_times = [r["bfs_time"] for r in results]

    x = range(len(labels))
    plt.figure(figsize=(9, 5))
    plt.bar([i - 0.2 for i in x], dfs_times, width=0.4, label="DFS (Stack)")
    plt.bar([i + 0.2 for i in x], bfs_times, width=0.4, label="BFS (Queue)")
    plt.xticks(x, labels)
    plt.ylabel("Execution Time (seconds)")
    plt.title("Graph Traversal Benchmark: DFS vs BFS")
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()
    plt.show()


def plot_flight_network(edges: List[Tuple[str, str]], max_edges: int = 100):
    """Draws a topological subgraph of flight connections."""
    g = build_nx_graph(edges[:max_edges])
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(g, seed=42)
    weights = nx.get_edge_attributes(g, "weight")

    nx.draw(
        g,
        pos,
        with_labels=True,
        node_size=700,
        node_color="#6BAED6",
        font_size=8,
        font_weight="bold",
    )
    nx.draw_networkx_edge_labels(g, pos, edge_labels=weights, font_size=7)
    plt.title(f"Flight Network Subgraph Topology (First {max_edges} routes)")
    plt.tight_layout()
    plt.show()