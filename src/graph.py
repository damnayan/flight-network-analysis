import csv
import time
from collections import defaultdict, deque
from typing import Dict, List, Optional, Set, Tuple


def read_airport_metadata(filename: str) -> Dict[str, str]:
    """
    Parses airports reference file (e.g. airport code -> airport name/details).
    Tries tab delimiter first, falls back to comma.
    """
    airport_names: Dict[str, str] = {}
    try:
        with open(filename, mode="r", encoding="utf-8", newline="") as f:
            sample = f.read(1024)
            delimiter = "\t" if "\t" in sample else ","
            f.seek(0)
            reader = csv.reader(f, delimiter=delimiter)
            for row in reader:
                if len(row) >= 2 and row[0].strip():
                    code = row[0].strip()
                    name = row[1].strip()
                    airport_names[code] = name
                elif len(row) == 1 and row[0].strip():
                    airport_names[row[0].strip()] = row[0].strip()
    except FileNotFoundError:
        pass
    return airport_names


def read_flight_data(
    filename: str, codes_file: Optional[str] = None
) -> Tuple[Set[str], List[Tuple[str, str]]]:
    """
    Parses TSV flight records into unique airports (nodes) and routes (edges).
    If codes_file is provided, initializes all known airports (including isolated ones).
    """
    nodes: Set[str] = set()
    edges: List[Tuple[str, str]] = []

    if codes_file:
        metadata = read_airport_metadata(codes_file)
        nodes.update(metadata.keys())

    with open(filename, mode="r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        next(reader, None)  # Skip header
        for row in reader:
            if len(row) >= 2 and row[0].strip() and row[1].strip():
                origin, dest = row[0].strip(), row[1].strip()
                nodes.add(origin)
                nodes.add(dest)
                edges.append((origin, dest))

    return nodes, edges


def build_adjacency_list(
    nodes: Set[str], edges: List[Tuple[str, str]]
) -> Dict[str, Set[str]]:
    """Builds an undirected graph represented as an adjacency list."""
    graph: Dict[str, Set[str]] = defaultdict(set)
    for node in nodes:
        graph[node]
    for origin, dest in edges:
        graph[origin].add(dest)
        graph[dest].add(origin)
    return graph


def dfs(start: str, visited: Set[str], graph: Dict[str, Set[str]]) -> List[str]:
    """Iterative Depth-First Search traversal using an explicit stack."""
    stack = [start]
    component = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return component


def bfs(start: str, visited: Set[str], graph: Dict[str, Set[str]]) -> List[str]:
    """Breadth-First Search traversal using collections.deque."""
    queue = deque([start])
    component = []
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return component


def find_connected_components(
    graph: Dict[str, Set[str]], method: str = "dfs"
) -> List[List[str]]:
    """Finds all connected components via DFS or BFS."""
    visited: Set[str] = set()
    components = []
    traverse = dfs if method == "dfs" else bfs

    for node in graph:
        if node not in visited:
            comp = traverse(node, visited, graph)
            components.append(comp)
    return components


def benchmark_traversal(graph: Dict[str, Set[str]]) -> Dict[str, float]:
    """Measures execution time for DFS vs BFS on the same graph."""
    start_dfs = time.perf_counter()
    cc_dfs = find_connected_components(graph, method="dfs")
    dfs_time = time.perf_counter() - start_dfs

    start_bfs = time.perf_counter()
    cc_bfs = find_connected_components(graph, method="bfs")
    bfs_time = time.perf_counter() - start_bfs

    return {
        "components": len(cc_dfs),
        "dfs_time": dfs_time,
        "bfs_time": bfs_time,
    }