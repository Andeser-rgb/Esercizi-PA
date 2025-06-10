from collections import deque


def can_remove(graph: list[list[int]]) -> bool:
    if len(graph) == 0:
        return False

    queue = deque()
    queue.append((None, 0))
    visited = [False] * len(graph)
    visited_num = 0
    cycle = False

    while not (len(queue) == 0):
        prev, el = queue.popleft()
        if visited[el]:
            cycle = True
            continue
        visited[el] = True
        visited_num += 1
        for child in graph[el]:
            if child == prev:
                continue
            queue.append((el, child))
    return cycle and (visited_num == len(graph))


# --- Test Cases ---

print("--- Running Test Cases for can_remove function ---")

# Test Case 1: Simple Graph (0-1-2 - a tree)
# Expected: False (No cycle)
graph1 = [[1], [0, 2], [1]]
print(f"\nGraph 1: {graph1}")
result1 = can_remove(graph1)
print(f"Result: {result1}, Expected: False")
assert result1 == False, "Test Case 1 Failed"

# Test Case 2: Graph with a Cycle (Triangle 0-1-2-0)
# Expected: True (Connected, has a cycle)
graph2 = [[1, 2], [0, 2], [0, 1]]
print(f"\nGraph 2: {graph2}")
result2 = can_remove(graph2)
print(f"Result: {result2}, Expected: True")
assert result2 == True, "Test Case 2 Failed"

# Test Case 3: Disconnected Graph (0-1 and 2-3)
# Expected: False (Not connected)
graph3 = [[1], [0], [3], [2]]
print(f"\nGraph 3: {graph3}")
result3 = can_remove(graph3)
print(f"Result: {result3}, Expected: False")
assert result3 == False, "Test Case 3 Failed"

# Test Case 4: Graph with a Bridge and other non-bridge edges
# (Square 0-1-2-3-0 with tail 3-4)
# Expected: True (Connected, has a cycle (the square))
graph4 = [[1, 3], [0, 2], [1, 3], [0, 2, 4], [3]]
print(f"\nGraph 4: {graph4}")
result4 = can_remove(graph4)
print(f"Result: {result4}, Expected: True")
assert result4 == True, "Test Case 4 Failed"

# Test Case 5: Single Node Graph
# Expected: False (No edges to remove, no cycle)
graph5 = [[]]
print(f"\nGraph 5: {graph5}")
result5 = can_remove(graph5)
print(f"Result: {result5}, Expected: False")
assert result5 == False, "Test Case 5 Failed"

# Test Case 6: Empty Graph
# Expected: False (No nodes, no edges)
graph6 = []
print(f"\nGraph 6: {graph6}")
result6 = can_remove(graph6)
print(f"Result: {result6}, Expected: False")
assert result6 == False, "Test Case 6 Failed"

# Test Case 7: Larger connected graph without a cycle (a larger tree)
# Expected: False
graph7 = [[1], [0, 2, 3], [1, 4], [1, 5], [2], [3]]
print(f"\nGraph 7: {graph7}")
result7 = can_remove(graph7)
print(f"Result: {result7}, Expected: False")
assert result7 == False, "Test Case 7 Failed"

# Test Case 8: Another larger connected graph with multiple cycles
# Expected: True
graph8 = [[1, 3], [0, 2, 4], [1, 3], [0, 2, 5], [1, 5], [3, 4]]
print(f"\nGraph 8: {graph8}")
result8 = can_remove(graph8)
print(f"Result: {result8}, Expected: True")
assert result8 == True, "Test Case 8 Failed"


print("\nAll test cases passed!")
