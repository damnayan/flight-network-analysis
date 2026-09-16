import pytest
from src.graph import build_adjacency_list, find_connected_components, dfs, bfs


@pytest.fixture
def sample_graph():
    # 2 components: {A, B, C} and {D, E}, plus isolated node F
    nodes = {"A", "B", "C", "D", "E", "F"}
    edges = [("A", "B"), ("B", "C"), ("D", "E")]
    return build_adjacency_list(nodes, edges)


def test_adjacency_list_structure(sample_graph):
    assert "B" in sample_graph["A"]
    assert "A" in sample_graph["B"]
    assert "C" in sample_graph["B"]
    assert sample_graph["F"] == set()


def test_dfs_single_component(sample_graph):
    visited = set()
    component = dfs("A", visited, sample_graph)
    assert set(component) == {"A", "B", "C"}
    assert visited == {"A", "B", "C"}


def test_bfs_single_component(sample_graph):
    visited = set()
    component = bfs("A", visited, sample_graph)
    assert set(component) == {"A", "B", "C"}
    assert visited == {"A", "B", "C"}


def test_connected_components_count(sample_graph):
    cc_dfs = find_connected_components(sample_graph, method="dfs")
    cc_bfs = find_connected_components(sample_graph, method="bfs")

    assert len(cc_dfs) == 3
    assert len(cc_bfs) == 3

    flat_dfs = {frozenset(c) for c in cc_dfs}
    expected = {frozenset({"A", "B", "C"}), frozenset({"D", "E"}), frozenset({"F"})}
    assert flat_dfs == expected