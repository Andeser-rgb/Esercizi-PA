from collections import deque

def maximum_distance_nodes(graph: list[list[int]], s: int):
    visited = [False] * len(graph)
    distances = [0] * len(graph)
    max_distance = 0
    q = deque()
    q.append(s)
    visited[s] = True

    while q:
        node = q.popleft()
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                q.append(child)
                distances[child] = distances[node] + 1
                max_distance = distances[child]

    res = []
    for i in range(len(graph)):
        if distances[i] == max_distance:
            res.append(i)
    return res


def run_test(name, func, args, expected_output):
    """
    Helper function to run a test case and print the result.
    """
    actual_output = func(*args)
    # Sort results for consistent comparison if order doesn't matter
    if isinstance(actual_output, list):
        actual_output = sorted(actual_output)
    if isinstance(expected_output, list):
        expected_output = sorted(expected_output)

    if actual_output == expected_output:
        print(f"✅ Test '{name}' PASSED.")
    else:
        print(f"❌ Test '{name}' FAILED.")
        print(f"   Input: graph={args[0]}, s={args[1]}")
        print(f"   Expected: {expected_output}")
        print(f"   Got:      {actual_output}")

# --- Test Cases ---

print("Running tests for maximum_distance_nodes:\n")

# Test 1: Simple line graph
# 0 -- 1 -- 2 -- 3
graph1 = [[1], [0, 2], [1, 3], [2]]
run_test("Simple Line Graph (start 0)", maximum_distance_nodes, (graph1, 0), [3])
run_test("Simple Line Graph (start 1)", maximum_distance_nodes, (graph1, 1), [3])
run_test("Simple Line Graph (start 3)", maximum_distance_nodes, (graph1, 3), [0])

# Test 2: Star graph
#   1
#   |
# 0-2-3
#   |
#   4
graph2 = [[2], [2], [0, 1, 3, 4], [2], [2]]
run_test("Star Graph (start 2)", maximum_distance_nodes, (graph2, 2), [0, 1, 3, 4])
run_test("Star Graph (start 0)", maximum_distance_nodes, (graph2, 0), [1, 3, 4]) # Max distance 2 from 0

# Test 3: Disconnected graph
# 0 -- 1   2 -- 3
graph3 = [[1], [0], [3], [2]]
run_test("Disconnected Graph (start 0)", maximum_distance_nodes, (graph3, 0), [1])
run_test("Disconnected Graph (start 2)", maximum_distance_nodes, (graph3, 2), [3])

# Test 4: Single node graph
graph4 = [[]]
run_test("Single Node Graph (start 0)", maximum_distance_nodes, (graph4, 0), [0])

# Test 5: Complex graph
# 0 --- 1 --- 2
# |     |     |
# 3 --- 4 --- 5
#       |
#       6
graph5 = [
    [1, 3],       # 0
    [0, 2, 4],    # 1
    [1, 5],       # 2
    [0, 4],       # 3
    [1, 3, 5, 6], # 4
    [2, 4],       # 5
    [4]           # 6
]
run_test("Complex Graph (start 0)", maximum_distance_nodes, (graph5, 0), [5, 6])
run_test("Complex Graph (start 6)", maximum_distance_nodes, (graph5, 6), [0, 2])
run_test("Complex Graph (start 4)", maximum_distance_nodes, (graph5, 4), [0, 2]) # Max distance 2 (from 4, 0 and 2 are furthest)

# Test 6: Graph with a cycle and multiple paths to same distance
# 0 --- 1
# | \   |
# 3 --- 2
graph6 = [
    [1, 2, 3],  # 0
    [0, 2],     # 1
    [0, 1, 3],  # 2
    [0, 2]      # 3
]
# From 0, all other nodes are distance 1. Max distance 1.
run_test("Graph with Cycle (start 0)", maximum_distance_nodes, (graph6, 0), [1, 2, 3])
# From 1, all other nodes are distance 1. Max distance 1.
run_test("Graph with Cycle (start 1)", maximum_distance_nodes, (graph6, 1), [3])

# Test 7: Graph where 's' is isolated (or not connected to anything)
graph7 = [[], [2], [1]] # Node 0 is isolated
run_test("Isolated Start Node (start 0)", maximum_distance_nodes, (graph7, 0), [0])

print("\nTests complete.")
