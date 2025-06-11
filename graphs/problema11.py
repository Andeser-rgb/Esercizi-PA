def outward_edges(graph: list[list[int]]) -> int:
    res = [0] * len(graph)
    for i, el in enumerate(graph):
        res[i] = len(el)
    return res
def inward_edges(graph: list[list[int]]) -> int:
    res = [0] * len(graph)
    for el in graph:
        for i in el:
            res[i] += 1
    return res


# --- Test Cases ---

print("--- Testing outward_edges ---")

# Graph 1: Empty Graph
graph_1 = []
expected_out_1 = []
result_out_1 = outward_edges(graph_1)
print(f"Graph 1 (Outward): {graph_1} -> {result_out_1} (Expected: {expected_out_1}) - {'PASSED' if result_out_1 == expected_out_1 else 'FAILED'}")

# Graph 2: Single Node, No Edges
graph_2 = [[]]
expected_out_2 = [0]
result_out_2 = outward_edges(graph_2)
print(f"Graph 2 (Outward): {graph_2} -> {result_out_2} (Expected: {expected_out_2}) - {'PASSED' if result_out_2 == expected_out_2 else 'FAILED'}")

# Graph 3: Two Nodes, One Edge (0 -> 1)
graph_3 = [[1], []]
expected_out_3 = [1, 0]
result_out_3 = outward_edges(graph_3)
print(f"Graph 3 (Outward): {graph_3} -> {result_out_3} (Expected: {expected_out_3}) - {'PASSED' if result_out_3 == expected_out_3 else 'FAILED'}")

# Graph 4: Three Nodes, Simple Path (0 -> 1 -> 2)
graph_4 = [[1], [2], []]
expected_out_4 = [1, 1, 0]
result_out_4 = outward_edges(graph_4)
print(f"Graph 4 (Outward): {graph_4} -> {result_out_4} (Expected: {expected_out_4}) - {'PASSED' if result_out_4 == expected_out_4 else 'FAILED'}")

# Graph 5: Three Nodes, Cycle (0 -> 1 -> 2 -> 0)
graph_5 = [[1], [2], [0]]
expected_out_5 = [1, 1, 1]
result_out_5 = outward_edges(graph_5)
print(f"Graph 5 (Outward): {graph_5} -> {result_out_5} (Expected: {expected_out_5}) - {'PASSED' if result_out_5 == expected_out_5 else 'FAILED'}")

# Graph 6: Four Nodes, Multiple Edges and Self-Loop
graph_6 = [
    [1, 2],    # Node 0 points to 1 and 2
    [0, 2],    # Node 1 points to 0 and 2
    [2],       # Node 2 points to itself
    [0]        # Node 3 points to 0
]
expected_out_6 = [2, 2, 1, 1]
result_out_6 = outward_edges(graph_6)
print(f"Graph 6 (Outward): {graph_6} -> {result_out_6} (Expected: {expected_out_6}) - {'PASSED' if result_out_6 == expected_out_6 else 'FAILED'}")

# Graph 7: Disconnected Components
graph_7 = [
    [1],  # Component 1: 0 -> 1
    [],
    [3],  # Component 2: 2 -> 3
    []
]
expected_out_7 = [1, 0, 1, 0]
result_out_7 = outward_edges(graph_7)
print(f"Graph 7 (Outward): {graph_7} -> {result_out_7} (Expected: {expected_out_7}) - {'PASSED' if result_out_7 == expected_out_7 else 'FAILED'}")


print("\n--- Testing inward_edges ---")

# Graph 1: Empty Graph
graph_1 = []
expected_in_1 = []
result_in_1 = inward_edges(graph_1)
print(f"Graph 1 (Inward): {graph_1} -> {result_in_1} (Expected: {expected_in_1}) - {'PASSED' if result_in_1 == expected_in_1 else 'FAILED'}")

# Graph 2: Single Node, No Edges
graph_2 = [[]]
expected_in_2 = [0]
result_in_2 = inward_edges(graph_2)
print(f"Graph 2 (Inward): {graph_2} -> {result_in_2} (Expected: {expected_in_2}) - {'PASSED' if result_in_2 == expected_in_2 else 'FAILED'}")

# Graph 3: Two Nodes, One Edge (0 -> 1)
graph_3 = [[1], []]
expected_in_3 = [0, 1]
result_in_3 = inward_edges(graph_3)
print(f"Graph 3 (Inward): {graph_3} -> {result_in_3} (Expected: {expected_in_3}) - {'PASSED' if result_in_3 == expected_in_3 else 'FAILED'}")

# Graph 4: Three Nodes, Simple Path (0 -> 1 -> 2)
graph_4 = [[1], [2], []]
expected_in_4 = [0, 1, 1]
result_in_4 = inward_edges(graph_4)
print(f"Graph 4 (Inward): {graph_4} -> {result_in_4} (Expected: {expected_in_4}) - {'PASSED' if result_in_4 == expected_in_4 else 'FAILED'}")

# Graph 5: Three Nodes, Cycle (0 -> 1 -> 2 -> 0)
graph_5 = [[1], [2], [0]]
expected_in_5 = [1, 1, 1]
result_in_5 = inward_edges(graph_5)
print(f"Graph 5 (Inward): {graph_5} -> {result_in_5} (Expected: {expected_in_5}) - {'PASSED' if result_in_5 == expected_in_5 else 'FAILED'}")

# Graph 6: Four Nodes, Multiple Edges and Self-Loop
graph_6 = [
    [1, 2],    # Node 0 points to 1 and 2
    [0, 2],    # Node 1 points to 0 and 2
    [2],       # Node 2 points to itself
    [0]        # Node 3 points to 0
]
expected_in_6 = [2, 1, 3, 0] # Corrected expected value for in-edges to node 2 (self-loop counts)
result_in_6 = inward_edges(graph_6)
print(f"Graph 6 (Inward): {graph_6} -> {result_in_6} (Expected: {expected_in_6}) - {'PASSED' if result_in_6 == expected_in_6 else 'FAILED'}")

# Graph 7: Disconnected Components
graph_7 = [
    [1],  # Component 1: 0 -> 1
    [],
    [3],  # Component 2: 2 -> 3
    []
]
expected_in_7 = [0, 1, 0, 1]
result_in_7 = inward_edges(graph_7)
print(f"Graph 7 (Inward): {graph_7} -> {result_in_7} (Expected: {expected_in_7}) - {'PASSED' if result_in_7 == expected_in_7 else 'FAILED'}")




