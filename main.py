import argparse
import os
from src.graph import (
    read_flight_data,
    build_adjacency_list,
    find_connected_components,
    benchmark_traversal,
)
from src.visualize import plot_benchmark_results, plot_flight_network

AIRPORTS_CODES_FILE = "data/airports_codes.txt"

DEFAULT_DATASETS = {
    "small": "data/flights_small.txt",
    "medium": "data/flights_medium.txt",
    "large": "data/flights_large.txt",
}


def parse_args():
    parser = argparse.ArgumentParser(
        description="Flight Network Connectivity & Graph Traversal CLI"
    )
    parser.add_argument(
        "--dataset",
        choices=["small", "medium", "large", "all"],
        default="all",
        help="Dataset size to run analysis on",
    )
    parser.add_argument(
        "--method",
        choices=["dfs", "bfs", "both"],
        default="both",
        help="Traversal algorithm to evaluate",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="Render execution time charts and network graph",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    print("=" * 65)
    print(" FLIGHT NETWORK GRAPH ANALYSIS & TRAVERSAL BENCHMARK")
    print("=" * 65)

    codes_path = AIRPORTS_CODES_FILE if os.path.exists(AIRPORTS_CODES_FILE) else None
    if codes_path:
        print(f"[*] Loaded airport codes reference: {codes_path}")

    targets = (
        DEFAULT_DATASETS.items()
        if args.dataset == "all"
        else [(args.dataset, DEFAULT_DATASETS[args.dataset])]
    )

    results = []
    sample_edges = []

    for name, path in targets:
        if not os.path.exists(path):
            print(f"[!] Warning: File {path} not found. Skipping.")
            continue

        print(f"\nProcessing [{name.upper()}] dataset -> {path}")
        nodes, edges = read_flight_data(path, codes_file=codes_path)
        graph = build_adjacency_list(nodes, edges)

        if not sample_edges and edges:
            sample_edges = edges

        if args.method == "both":
            stats = benchmark_traversal(graph)
            results.append(
                {
                    "dataset": name,
                    "components": stats["components"],
                    "dfs_time": stats["dfs_time"],
                    "bfs_time": stats["bfs_time"],
                }
            )
            print(f"  • Total Airports (Nodes): {len(nodes)}")
            print(f"  • Total Routes (Edges):   {len(edges)}")
            print(f"  • Connected Components:   {stats['components']}")
            print(f"  • DFS Runtime:            {stats['dfs_time']:.5f} s")
            print(f"  • BFS Runtime:            {stats['bfs_time']:.5f} s")
        else:
            components = find_connected_components(graph, method=args.method)
            print(f"  • Total Airports (Nodes): {len(nodes)}")
            print(f"  • Total Routes (Edges):   {len(edges)}")
            print(f"  • Connected Components ({args.method.upper()}): {len(components)}")

    if args.plot and results:
        plot_benchmark_results(results)
        if sample_edges:
            plot_flight_network(sample_edges)


if __name__ == "__main__":
    main()