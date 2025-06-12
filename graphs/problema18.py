from collections import deque

def well_colored(graph: list[list[int]], colors: list[int]):
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] == 1 and (colors[i] == colors[j]):
                return False
            
    return True

def well_colored_adj(graph: list[list[int]], colors: list[int]):
    for i, adj_l in enumerate(graph):
        for j in adj_l:
            if colors[i] == colors[j]:
                return False
            
    return True
                

       
