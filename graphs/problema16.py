from collections import deque

def count_connected_components(graph: list[list[int]]):
    visited = [False] * len(graph)
    cc = 0
    for i in range(len(graph)):
        if not visited[i]:
            dfs(graph, i, visited)
            cc += 1
    return cc

       
def dfs(graph: list[list[int]], node: int, visited: list[bool]):
    visited[node] = True

    for child in graph[node]:
        if not visited[child]:
            dfs(graph, child, visited)
