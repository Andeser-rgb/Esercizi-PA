from collections import deque
import math

def diamater_and_radius(graph: list[list[int]]) -> (int, int):
    if not graph:
        return 0, 0
    # BFS to check if it is connected
    q = deque()
    q.append(0)
    visited = [False] * len(graph)
    nodes = 0
    while q:
        cnode = q.popleft()
        if visited[cnode]:
            continue
        visited[cnode] = True
        nodes += 1
        for child in graph[cnode]:
            q.append(child)

    if nodes != len(graph):
        return math.inf, math.inf

    # Calculate eccentricity of every nodes
    eccentricities = [0] * len(graph)
    for node in range(len(graph)):
        q = deque()
        q.append((node, 0))
        visited = [False] * len(graph)
        while q:
            cnode, dist = q.popleft()
            if visited[cnode]:
                continue
            visited[cnode] = True
            eccentricities[node] = max(eccentricities[node], dist)
            for child in graph[cnode]:
                q.append((child, dist + 1))

    radius = min(eccentricities)
    diameter = max(eccentricities)

        
    return diameter, radius




# Test Cases
print("--- Test Cases ---")

# Test 1: Single node graph
graph1 = [[]]
diameter1, radius1 = diamater_and_radius(graph1)
print(f"Graph 1 (Single Node): Diameter = {diameter1}, Radius = {radius1}") # Expected: (0, 0)

# Test 2: Two connected nodes
graph2 = [[1], [0]]
diameter2, radius2 = diamater_and_radius(graph2)
print(f"Graph 2 (Two Nodes): Diameter = {diameter2}, Radius = {radius2}") # Expected: (1, 1)

# Test 3: Simple path graph (3 nodes: 0-1-2)
graph3 = [[1], [0, 2], [1]]
diameter3, radius3 = diamater_and_radius(graph3)
print(f"Graph 3 (Path 3 Nodes): Diameter = {diameter3}, Radius = {radius3}") # Expected: (2, 1)

# Test 4: Simple path graph (4 nodes: 0-1-2-3)
graph4 = [[1], [0, 2], [1, 3], [2]]
diameter4, radius4 = diamater_and_radius(graph4)
print(f"Graph 4 (Path 4 Nodes): Diameter = {diameter4}, Radius = {radius4}") # Expected: (3, 2)

# Test 5: Star graph (center node 0 connected to 1, 2, 3)
graph5 = [[1, 2, 3], [0], [0], [0]]
diameter5, radius5 = diamater_and_radius(graph5)
print(f"Graph 5 (Star Graph): Diameter = {diameter5}, Radius = {radius5}") # Expected: (2, 1)

# Test 6: Cycle graph (3 nodes: 0-1-2-0)
graph6 = [[1, 2], [0, 2], [0, 1]]
diameter6, radius6 = diamater_and_radius(graph6)
print(f"Graph 6 (Cycle 3 Nodes): Diameter = {diameter6}, Radius = {radius6}") # Expected: (1, 1)

# Test 7: Cycle graph (4 nodes: 0-1-2-3-0)
graph7 = [[1, 3], [0, 2], [1, 3], [0, 2]]
diameter7, radius7 = diamater_and_radius(graph7)
print(f"Graph 7 (Cycle 4 Nodes): Diameter = {diameter7}, Radius = {radius7}") # Expected: (2, 2)

# Test 8: Disconnected graph
graph8 = [[1], [0], [3], [2]] # Two separate components: 0-1 and 2-3
diameter8, radius8 = diamater_and_radius(graph8)
print(f"Graph 8 (Disconnected): Diameter = {diameter8}, Radius = {radius8}") # Expected: (inf, inf)

# Test 9: Complete graph (K4)
graph9 = [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]]
diameter9, radius9 = diamater_and_radius(graph9)
print(f"Graph 9 (Complete K4): Diameter = {diameter9}, Radius = {radius9}") # Expected: (1, 1)

# Test 10: Empty graph (no nodes)
graph10 = []
diameter10, radius10 = diamater_and_radius(graph10)
print(f"Graph 10 (Empty): Diameter = {diameter10}, Radius = {radius10}") # Expected: (0, 0)
