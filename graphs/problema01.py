def contiene_cicli(grafo):
    visitato = {nodo: False for nodo in grafo}
    genitore = {nodo: None for nodo in grafo}

    for nodo_corrente in grafo:
        if not visitato[nodo_corrente]:
            if _dfs_ricerca_cicli_semplificato(
                nodo_corrente, None, visitato, genitore, grafo
            ):
                return True

    return False


def _dfs_ricerca_cicli_semplificato(u, parent_node, visitato, genitore, grafo):
    visitato[u] = True
    genitore[u] = parent_node

    for v in grafo[u]:
        if not visitato[v]:
            if _dfs_ricerca_cicli_semplificato(v, u, visitato, genitore, grafo):
                return True
        elif v != genitore[u]:
            return True

    return False


grafo_senza_cicli = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B"],
    "E": ["C"],
}
print(f"Grafo senza cicli: {contiene_cicli(grafo_senza_cicli)}")  # Output atteso: False

grafo_con_ciclo = {"A": ["B", "D"], "B": ["A", "C"], "C": ["B", "D"], "D": ["A", "C"]}
print(f"Grafo con ciclo: {contiene_cicli(grafo_con_ciclo)}")  # Output atteso: True

# Grafo disconnesso con un ciclo in una componente
grafo_disconnesso_con_ciclo = {
    "X": ["Y", "Z"],
    "Y": ["X", "Z"],
    "Z": ["X", "Y"],
    "P": ["Q"],
    "Q": ["P"],
}
print(
    f"Grafo disconnesso con ciclo: {contiene_cicli(grafo_disconnesso_con_ciclo)}"
)  # Output atteso: True

# Grafo disconnesso senza cicli
grafo_disconnesso_senza_cicli = {
    "X": ["Y"],
    "Y": ["X"],
    "P": ["Q"],
    "Q": ["P"],
    "R": [],
}
print(
    f"Grafo disconnesso senza cicli: {contiene_cicli(grafo_disconnesso_senza_cicli)}"
)  # Output atteso: False

# Grafo con un solo nodo (no cicli)
grafo_un_nodo = {"A": []}
print(f"Grafo con un nodo: {contiene_cicli(grafo_un_nodo)}")  # Output atteso: False

# Grafo vuoto
grafo_vuoto = {}
print(f"Grafo vuoto: {contiene_cicli(grafo_vuoto)}")  # Output atteso: False
