\# Flight Network Connectivity \& Graph Traversal Analysis



An algorithmic benchmarking tool modeling global flight routes as undirected graphs to evaluate connectivity, isolated clusters, and traversal efficiency across varied dataset scales.



\---



\## Key Highlights

\* \*\*Zero-Dependency Core:\*\* Custom adjacency list structures and traversals built purely with standard library primitives (`collections.deque`, `defaultdict`).

\* \*\*Graph Traversal Implementations:\*\* Iterative stack-based Depth-First Search (DFS) and queue-based Breadth-First Search (BFS) finding connected components in $O(V + E)$ time.

\* \*\*Airport Metadata Resolution:\*\* Robust ingestion handling isolated airport nodes via code dictionaries.

\* \*\*Empirical Benchmarking:\*\* Real-time profiling across topologies scaling up to 330,000+ airports and routes.

\* \*\*CLI \& Automated Testing:\*\* Command-line flags for targeted execution, complemented by a full `pytest` suite.



\---



\## Algorithmic Complexity



| Algorithm | Data Structure | Time Complexity | Space Complexity |

| :--- | :--- | :--- | :--- |

| \*\*Iterative DFS\*\* | Auxiliary Stack (Python list) | $O(V + E)$ | $O(V)$ |

| \*\*Iterative BFS\*\* | FIFO Queue (`collections.deque`) | $O(V + E)$ | $O(V)$ |



\---



\## Benchmark Results



Empirical execution benchmarks measured on local environment:



| Dataset | Airports ($V$) | Routes ($E$) | Connected Components | DFS Time | BFS Time |

| :--- | :--- | :--- | :--- | :--- | :--- |

| \*\*Small\*\* | 50,001 | 50,000 | 1 | \~0.028 s | \~0.026 s |

| \*\*Medium\*\* | 100,001 | 100,000 | 1 | \~0.070 s | \~0.068 s |

| \*\*Large\*\* | 336,776 | 336,776 | 1 | \~0.327 s | \~0.287 s |



\---



\## Project Structure



```text

flight-network-analysis/

├── data/

│   ├── airport\_codes.txt     # Reference airport codes

│   ├── flights\_small.txt     # 50k routes dataset

│   ├── flights\_medium.txt    # 100k routes dataset

│   └── flights\_large.txt     # 336k routes dataset

├── src/

│   ├── \_\_init\_\_.py

│   ├── graph.py              # Parsing, adjacency representation, DFS/BFS logic

│   └── visualize.py          # Benchmark plotting \& NetworkX visualization

├── tests/

│   ├── \_\_init\_\_.py

│   └── test\_graph.py         # Pytest verification suite

├── main.py                   # CLI entry point

├── requirements.txt

└── README.md

