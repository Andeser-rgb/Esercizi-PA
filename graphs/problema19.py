from collections import deque

def is_vertex_cover(graph: list[list[int]], s: list[int]):
    contains = [False] * len(graph)
    for el in s:
        contains[el] = True

    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if contains[i] == 0 and contains[j] == 0:
                return False
    return True


def is_vertex_cover_adj(graph: list[list[int]], s: list[int]):
    contains = [False] * len(graph)
    for el in s:
        contains[el] = True

    for i, adj_l in enumerate(graph):
        for j in adj_l:
            if contains[i] == 0 and contains[j] == 0:
                return False
    return True
       
