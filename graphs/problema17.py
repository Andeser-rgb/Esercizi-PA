from collections import deque

def triangles(graph: list[list[int]]):
    tr = 0
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            for k in range(j + 1, len(graph)):
                if graph[i][j] == 1 and graph[j][k] == 1 and graph[k][i] == 1:
                    tr += 1
    return tr
                

       
def dfs(graph: list[list[int]], node: int, visited: list[bool]):
    visited[node] = True

    for child in graph[node]:
        if not visited[child]:
            dfs(graph, child, visited)
