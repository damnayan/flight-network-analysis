# Flight Network Connectivity & Graph Traversal Analysis

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Algorithms](https://img.shields.io/badge/Algorithms-DFS%20%7C%20BFS-orange.svg)]()
[![Performance](https://img.shields.io/badge/Runtime-%3C0.3s-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()

An algorithmic benchmarking tool modeling global flight routes as undirected graphs to evaluate network connectivity, isolated clusters, and traversal efficiency across varied dataset scales.

---

## Key Highlights

- **Zero-Dependency Core:** Custom adjacency list representations and graph traversals built purely with Python standard library primitives (`collections.deque`, `defaultdict`).
- **Graph Traversal Implementations:** Iterative stack-based Depth-First Search (DFS) and queue-based Breadth-First Search (BFS) computing connected components in strictly linear time.
- **Airport Metadata Resolution:** Robust ingestion pipeline resolving isolated airport nodes against standardized IATA/ICAO code dictionaries.
- **Empirical Benchmarking:** Real-time profiling across graph topologies scaling up to 336,000+ airports and routes.
- **CLI & Automated Testing:** Flexible command-line flags for targeted execution, accompanied by a full `pytest` verification suite.

---

## Algorithmic Complexity

| Algorithm | Data Structure | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Iterative DFS** | Auxiliary Stack (Python list) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| **Iterative BFS** | FIFO Queue (`collections.deque`) | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |

---

## Benchmark Results

Empirical execution benchmarks measured on local environment across scaling dataset sizes:

| Dataset Scale | Airports ($V$) | Routes ($E$) | Connected Components | DFS Time | BFS Time |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Small** | 50,001 | 50,000 | 1 | ~0.028 s | ~0.026 s |
| **Medium** | 100,001 | 100,000 | 1 | ~0.070 s | ~0.068 s |
| **Large** | 336,776 | 336,776 | 1 | ~0.327 s | **~0.287 s** |

---

## Project Structure

```text
flight-network-analysis/
├── data/
│   ├── airport_codes.txt     # Reference airport codes
│   ├── flights_small.txt     # 50k routes dataset
│   ├── flights_medium.txt    # 100k routes dataset
│   └── flights_large.txt     # 336k routes dataset
├── src/
│   ├── __init__.py
│   ├── graph.py              # Parsing, adjacency representation, DFS/BFS logic
│   └── visualize.py          # Benchmark plotting & NetworkX visualization
├── tests/
│   ├── __init__.py
│   └── test_graph.py         # Pytest verification suite
├── main.py                   # CLI entry point
├── requirements.txt
└── README.md
