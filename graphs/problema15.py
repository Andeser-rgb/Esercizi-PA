from collections import deque

def count_nodes_at_distance(graph: list[list[int]], v:int, k: int):
    if not graph:
        return 0
    visited = [False] * len(graph)
    q = deque()
    q.append((v, 0))
    visited[v] = True
    count = 0

    while q:
        node, dist = q.popleft()
        if dist > k:
            break
        count += 1
        for c in graph[node]:
            if not visited[c]:
                visited[c] = True
                q.append((c, dist + 1))

    return count

        
def test_count_nodes_at_distance():
    print("\nRunning tests for count_nodes_at_distance function...")

    # Grafo di esempio per i test di distanza
    # 0 -> 1 -> 2 -> 3
    # |    ^
    # v    |
    # 4 <---
    graph_dist = [
        [1, 4],
        [2],
        [3],
        [],
        [1]
    ]
    # Nodi: 0, 1, 2, 3, 4

    # Test Case 1: k = 0
    # Da nodo 0, k=0 -> solo nodo 0
    assert count_nodes_at_distance(graph_dist, 0, 0) == 1, "Test distanza 1 Fallito"
    print("Test distanza 1 Passato: k=0")

    # Test Case 2: k = 1 da nodo 0
    # Nodi raggiungibili da 0 a distanza 1: {0, 1, 4}
    assert count_nodes_at_distance(graph_dist, 0, 1) == 3, "Test distanza 2 Fallito"
    print("Test distanza 2 Passato: k=1 da nodo 0")

    # Test Case 3: k = 2 da nodo 0
    # Nodi raggiungibili da 0 a distanza 2: {0, 1, 4, 2} (0->1->2, 0->4->1)
    assert count_nodes_at_distance(graph_dist, 0, 2) == 4, "Test distanza 3 Fallito"
    print("Test distanza 3 Passato: k=2 da nodo 0")

    # Test Case 4: k = 3 da nodo 0
    # Nodi raggiungibili da 0 a distanza 3: {0, 1, 4, 2, 3} (0->1->2->3)
    assert count_nodes_at_distance(graph_dist, 0, 3) == 5, "Test distanza 4 Fallito"
    print("Test distanza 4 Passato: k=3 da nodo 0")

    # Test Case 5: k = 4 da nodo 0 (o qualsiasi k >= max_dist)
    assert count_nodes_at_distance(graph_dist, 0, 4) == 5, "Test distanza 5 Fallito"
    print("Test distanza 5 Passato: k=4 da nodo 0 (tutti raggiungibili)")

    # Test Case 6: Da nodo 3 (foglia), k=0
    assert count_nodes_at_distance(graph_dist, 3, 0) == 1, "Test distanza 6 Fallito"
    print("Test distanza 6 Passato: nodo foglia k=0")

    # Test Case 7: Da nodo 3 (foglia), k=10 (o qualsiasi k)
    assert count_nodes_at_distance(graph_dist, 3, 10) == 1, "Test distanza 7 Fallito"
    print("Test distanza 7 Passato: nodo foglia k=10")
    
    # Test Case 8: Grafo vuoto
    assert count_nodes_at_distance([], 0, 1) == 0, "Test distanza 8 Fallito: grafo vuoto"
    print("Test distanza 8 Passato: grafo vuoto")

    # Test Case 9: Nodo non valido
    try:
        count_nodes_at_distance(graph_dist, 10, 1)
        assert False, "Test distanza 9 Fallito: Nessuna eccezione per nodo non valido"
    except IndexError:
        assert True, "Test distanza 9 Passato: Eccezione gestita per nodo non valido"
    print("Test distanza 9 Passato: Nodo non valido")
    

    print("\nAll tests for count_nodes_at_distance function passed!")

test_count_nodes_at_distance()

