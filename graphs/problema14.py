from collections import deque

def reachable(graph: list[list[int]]) -> list[int]:
    """
    Calcola il numero di nodi raggiungibili da ogni nodo in un grafo diretto.
    Utilizza l'algoritmo di Kosaraju per le Componenti Fortemente Connesse (SCC)
    e l'ordinamento topologico del grafo condensato per un'efficienza O(|V| + |E|).

    Args:
        graph: Rappresentazione del grafo come lista di adiacenza.
               graph[i] è una lista di interi che rappresenta i vicini del nodo i.
               Si assume che i nodi siano indicizzati da 0 a n-1, dove n è il numero di nodi.

    Returns:
        Una lista di interi, dove result[i] è il numero di nodi raggiungibili
        dal nodo i.
    """
    n = len(graph)  # Numero di nodi nel grafo

    # --- Passaggio 1: Prima DFS sul grafo originale per i tempi di completamento ---
    visited = [False] * n
    finish_order_stack = [] # Stack per memorizzare i nodi in ordine di completamento (post-order)

    def dfs1(u: int):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        finish_order_stack.append(u) # Aggiungi u allo stack solo dopo aver visitato tutti i suoi discendenti

    # Esegui la prima DFS per tutti i nodi
    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # --- Passaggio 2: Costruisci il grafo trasposto (G_T) ---
    # Inverti la direzione di tutti gli archi del grafo originale
    graph_t = [[] for _ in range(n)]
    for u in range(n):
        for v in graph[u]:
            graph_t[v].append(u)

    # --- Passaggio 3: Seconda DFS su G_T nell'ordine inverso dei tempi di completamento ---
    visited = [False] * n  # Resetta l'array dei nodi visitati
    sccs = []              # Lista per memorizzare le SCC trovate
    scc_id = [-1] * n      # Mappa nodo_originale -> ID_SCC
    scc_count = 0          # Contatore per gli ID delle SCC

    def dfs2(u: int, current_scc: list[int]):
        visited[u] = True
        scc_id[u] = scc_count # Assegna l'ID della SCC corrente al nodo
        current_scc.append(u)
        for v in graph_t[u]: # Esplora nel grafo trasposto
            if not visited[v]:
                dfs2(v, current_scc)

    # Elabora i nodi dallo stack in ordine inverso di completamento
    while finish_order_stack:
        u = finish_order_stack.pop() # Estrai i nodi uno alla volta
        if not visited[u]:
            current_scc = []
            dfs2(u, current_scc)
            sccs.append(current_scc)
            scc_count += 1

    # --- Passaggio 4: Costruisci il Grafo Condensato (DAG delle SCC) ---
    scc_graph = [[] for _ in range(scc_count)]  # Lista di adiacenza del grafo condensato
    scc_sizes = [0] * scc_count                 # Dimensione di ogni SCC (numero di nodi originali)
    
    # Inizializza le dimensioni delle SCC
    for i in range(scc_count):
        scc_sizes[i] = len(sccs[i])

    # Aggiungi archi al grafo condensato
    # Usiamo un set per evitare archi duplicati tra SCC
    scc_edges = set() 
    for u in range(n):
        for v in graph[u]:
            u_scc = scc_id[u]
            v_scc = scc_id[v]
            if u_scc != v_scc:
                if (u_scc, v_scc) not in scc_edges:
                    scc_graph[u_scc].append(v_scc)
                    scc_edges.add((u_scc, v_scc))

    # --- Passaggio 5: Calcola i Nodi Raggiungibili per Ogni SCC nel Grafo Condensato ---
    # Usiamo la memoizzazione per calcolare il numero di nodi raggiungibili da ciascuna SCC
    scc_reachable_memo = {}  # Mappa ID_SCC -> numero totale di nodi originali raggiungibili

    def dfs_condensed(scc_idx: int) -> int:
        """
        DFS sul grafo condensato per calcolare il numero totale di nodi originali
        raggiungibili da una data SCC.
        """
        if scc_idx in scc_reachable_memo:
            return scc_reachable_memo[scc_idx]

        # Inizialmente, il conteggio include solo i nodi all'interno di questa SCC
        current_reachable_count = scc_sizes[scc_idx]

        # Aggiungi i nodi raggiungibili dalle SCC vicine
        for neighbor_scc_idx in scc_graph[scc_idx]:
            current_reachable_count += dfs_condensed(neighbor_scc_idx)

        scc_reachable_memo[scc_idx] = current_reachable_count
        return current_reachable_count

    # Avvia la DFS sul grafo condensato per ogni SCC
    for i in range(scc_count):
        dfs_condensed(i)

    # --- Passaggio 6: Assegna i Risultati ai Nodi Originali ---
    result = [0] * n
    for i in range(n):
        result[i] = scc_reachable_memo[scc_id[i]]

    return result


# --- Test cases per la funzione reachable ---
def test_reachable():
    print("Running tests for reachable function...")

    # Test Case 1: Grafo vuoto
    graph1 = []
    expected1 = []
    result1 = reachable(graph1)
    assert result1 == expected1, f"Test 1 Fallito: Atteso {expected1}, Ottenuto {result1}"
    print(f"Test 1 Passato: Grafo vuoto. Risultato: {result1}")

    # Test Case 2: Grafo con un singolo nodo (senza archi)
    graph2 = [[]]
    expected2 = [1]
    result2 = reachable(graph2)
    assert result2 == expected2, f"Test 2 Fallito: Atteso {expected2}, Ottenuto {result2}"
    print(f"Test 2 Passato: Singolo nodo senza archi. Risultato: {result2}")

    # Test Case 3: Grafo semplice diretto (come nell'esempio precedente)
    # A -> B, A -> C, B -> C, C -> D
    graph3 = [[1, 2], [2], [3], []]
    # Nodi: 0, 1, 2, 3 (A, B, C, D)
    # SCCs: {0}, {1}, {2}, {3}
    # Reachable from 0 (A): {0, 1, 2, 3} -> 4
    # Reachable from 1 (B): {1, 2, 3} -> 3
    # Reachable from 2 (C): {2, 3} -> 2
    # Reachable from 3 (D): {3} -> 1
    expected3 = [4, 3, 2, 1]
    result3 = reachable(graph3)
    assert result3 == expected3, f"Test 3 Fallito: Atteso {expected3}, Ottenuto {result3}"
    print(f"Test 3 Passato: Grafo semplice diretto. Risultato: {result3}")

    # Test Case 4: Grafo con una SCC
    # 0 <-> 1 (ciclo), 1 -> 2, 2 -> 3
    graph4 = [[1], [0, 2], [3], []]
    # Nodi: 0, 1, 2, 3
    # SCCs: {0, 1}, {2}, {3}
    # Reachable from 0: {0, 1, 2, 3} -> 4
    # Reachable from 1: {0, 1, 2, 3} -> 4
    # Reachable from 2: {2, 3} -> 2
    # Reachable from 3: {3} -> 1
    expected4 = [4, 4, 2, 1]
    result4 = reachable(graph4)
    assert result4 == expected4, f"Test 4 Fallito: Atteso {expected4}, Ottenuto {result4}"
    print(f"Test 4 Passato: Grafo con una SCC. Risultato: {result4}")

    # Test Case 5: Grafo disconnesso con più SCC
    # 0 -> 1, 1 -> 0
    # 2 -> 3
    # 4
    graph5 = [[1], [0], [3], [], []]
    # Nodi: 0, 1, 2, 3, 4
    # SCCs: {0, 1}, {2}, {3}, {4}
    # Reachable from 0: {0, 1} -> 2
    # Reachable from 1: {0, 1} -> 2
    # Reachable from 2: {2, 3} -> 2
    # Reachable from 3: {3} -> 1
    # Reachable from 4: {4} -> 1
    expected5 = [2, 2, 2, 1, 1]
    result5 = reachable(graph5)
    assert result5 == expected5, f"Test 5 Fallito: Atteso {expected5}, Ottenuto {result5}"
    print(f"Test 5 Passato: Grafo disconnesso con più SCC. Risultato: {result5}")

    # Test Case 6: Grafo a catena lunga
    # 0 -> 1 -> 2 -> 3 -> 4
    graph6 = [[1], [2], [3], [4], []]
    expected6 = [5, 4, 3, 2, 1]
    result6 = reachable(graph6)
    assert result6 == expected6, f"Test 6 Fallito: Atteso {expected6}, Ottenuto {result6}"
    print(f"Test 6 Passato: Grafo a catena lunga. Risultato: {result6}")

    # Test Case 7: Grafo completo diretto (ogni nodo punta a tutti gli altri)
    # Tutti i nodi formano una singola SCC
    graph7 = [[j for j in range(5) if j != i] for i in range(5)]
    expected7 = [5, 5, 5, 5, 5]
    result7 = reachable(graph7)
    assert result7 == expected7, f"Test 7 Fallito: Atteso {expected7}, Ottenuto {result7}"
    print(f"Test 7 Passato: Grafo completo diretto. Risultato: {result7}")

    print("\nAll tests passed!")

# Esegui i test se lo script viene eseguito direttamente
if __name__ == "__main__":
    test_reachable()
