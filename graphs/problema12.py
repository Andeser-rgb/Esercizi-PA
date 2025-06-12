def squared_graph(graph: list[list[int]]):
    s_graph = [[0] * len(graph)] * len(graph)
    for i in range(len(graph)): 
        for j in range(len(graph)):
            if graph[i][j] == 1:
                for k in range(len(graph)):
                    s_graph[i][k] |= 1
        
    return s_graph
