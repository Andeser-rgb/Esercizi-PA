def esiste_cammino(grafo, u, v, w):
    visitato = {nodo: False for nodo in grafo}
    e1 = _dfs_esiste_cammino(u, w, visitato, grafo)
    visitato = {nodo: False for nodo in grafo}
    e2 = _dfs_esiste_cammino(v, w, visitato, grafo)

    return e1 and e2


def _dfs_esiste_cammino(a, b, visitato, grafo):
    if a == b:
        return True

    visitato[a] = True

    for v in grafo[a]:
        if not visitato[v]:
            if _dfs_esiste_cammino(v, b, visitato, grafo):
                return True

    return False


# --- Test con esempi ---

grafo_test = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E", "G"],
    "G": ["F"],
    "H": [],  # Nodo isolato
}

print("--- Test della funzione esiste_cammino_passando_per_dfs ---")

# Test Case 1: Cammino semplice esistente (A -> B -> E -> F -> G)
# u='A', v='G', w='E'
print(
    f"A -> G passando per E: {esiste_cammino(grafo_test, 'A', 'G', 'E')}"
)  # Atteso: True

# Test Case 2: Cammino semplice esistente (A -> C -> F -> G)
# u='A', v='G', w='C'
print(
    f"A -> G passando per C: {esiste_cammino(grafo_test, 'A', 'G', 'C')}"
)  # Atteso: True

# Test Case 3: Cammino non esistente (W non raggiungibile da U)
# u='A', v='D', w='H' (H è isolato)
print(
    f"A -> D passando per H: {esiste_cammino(grafo_test, 'A', 'D', 'H')}"
)  # Atteso: False

# Test Case 4: Cammino non esistente (V non raggiungibile da W)
# u='A', v='H', w='B' (H è isolato)
print(
    f"A -> H passando per B: {esiste_cammino(grafo_test, 'A', 'H', 'B')}"
)  # Atteso: False

# Test Case 5: W è il nodo di partenza (u = w)
# u='A', v='D', w='A' (Cammino A -> B -> D)
print(
    f"A -> D passando per A: {esiste_cammino(grafo_test, 'A', 'D', 'A')}"
)  # Atteso: True (A può raggiungere A, e A può raggiungere D)

# Test Case 6: W è il nodo di arrivo (v = w)
# u='A', v='C', w='C' (Cammino A -> C)
print(
    f"A -> C passando per C: {esiste_cammino(grafo_test, 'A', 'C', 'C')}"
)  # Atteso: True (A può raggiungere C, e C può raggiungere C)

# Test Case 7: Caso in cui u, v, w sono lo stesso nodo
# u='A', v='A', w='A'
print(
    f"A -> A passando per A: {esiste_cammino(grafo_test, 'A', 'A', 'A')}"
)  # Atteso: True
