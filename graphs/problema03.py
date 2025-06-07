def esiste_cammino_bidirezionale(grafo, u, v):
    visitato = {nodo: False for nodo in grafo}
    e1 = _dfs_esiste_cammino(u, v, visitato, grafo)
    visitato = {nodo: False for nodo in grafo}
    e2 = _dfs_esiste_cammino(v, u, visitato, grafo)

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


# --- Grafo Orientato di Test ---
grafo_orientato_test = {
    "A": ["B"],
    "B": ["C"],
    "C": ["D", "A"],  # C -> D e C -> A (crea un ciclo A-B-C-A)
    "D": [],
    "E": ["F"],
    "F": ["G"],
    "G": [],
}

print("--- Test per l'algoritmo 'esiste_cammino_bidirezionale' con grafo orientato ---")
print("Verifica: esiste un cammino da u a v E un cammino da v a u?")

# Test Case 1: A e D (A->B->C->D, D non ha vicini)
# u->v (A->D): True
# v->u (D->A): False
# Atteso: False
print(
    f"A <-> D: {esiste_cammino_bidirezionale(grafo_orientato_test, 'A', 'D')}"
)  # Output: False

# Test Case 2: A e C (A->B->C, C->A)
# u->v (A->C): True
# v->u (C->A): True
# Atteso: True (A e C sono fortemente connessi)
print(
    f"A <-> C: {esiste_cammino_bidirezionale(grafo_orientato_test, 'A', 'C')}"
)  # Output: True

# Test Case 3: E e G (E->F->G, G non ha vicini)
# u->v (E->G): True
# v->u (G->E): False
# Atteso: False
print(
    f"E <-> G: {esiste_cammino_bidirezionale(grafo_orientato_test, 'E', 'G')}"
)  # Output: False

# Test Case 4: D e A (D non ha vicini, A può raggiungere D ma D non può raggiungere A)
# u->v (D->A): False
# v->u (A->D): True
# Atteso: False
print(
    f"D <-> A: {esiste_cammino_bidirezionale(grafo_orientato_test, 'D', 'A')}"
)  # Output: False


# Test Case 6: Stesso nodo (A <-> A)
# u->v (A->A): True (cammino banale)
# v->u (A->A): True (cammino banale)
# Atteso: True
print(
    f"A <-> A: {esiste_cammino_bidirezionale(grafo_orientato_test, 'A', 'A')}"
)  # Output: True

# Test Case 7: Nodi in componenti sconnesse ma che si possono raggiungere a vicenda (se fosse un non orientato)
# ma in orientato non si raggiungono
grafo_orientato_sconnesso = {"1": ["2"], "2": ["1"], "3": ["4"], "4": ["3"]}
print(
    f"1 <-> 2 (grafo_orientato_sconnesso): {esiste_cammino_bidirezionale(grafo_orientato_sconnesso, '1', '2')}"
)  # Atteso: True
print(
    f"1 <-> 3 (grafo_orientato_sconnesso): {esiste_cammino_bidirezionale(grafo_orientato_sconnesso, '1', '3')}"
)  # Atteso: False (1->2, 3->4, ma 1 non raggiunge 3)
