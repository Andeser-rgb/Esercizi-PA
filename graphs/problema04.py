def trova_pozzo(graph: list[list[int]]) -> int:
    if len(graph) == 0:
        return None
    i = 0
    for j in range(len(graph)):
        if j == i:
            continue
        if graph[i][j] == 1:
            i = j
    for j in range(len(graph)):
        if j == i:
            continue
        if graph[i][j] == 1:
            return None
    for j in range(len(graph)):
        if j == i:
            continue
        if graph[j][i] == 0:
            return None
    return i


# --- Test Cases ---

# A '1' means a connection exists (i knows j), a '0' means it does not.

print("--- Test Case 1: Graph with a clear pozzo (node 2) ---")
# Node 2 knows no one (row 2 is all 0s).
# Everyone else knows node 2 (column 2 is all 1s).
graph1 = [[0, 1, 1, 0], [0, 0, 1, 0], [0, 0, 0, 0], [1, 0, 1, 0]]
print(f"Graph: {graph1}")
result1 = trova_pozzo(graph1)
print(f"Actual Result: {result1}")
print("Expected Result for a pozzo: 2\n")


print("--- Test Case 2: Graph with no pozzo (a cycle) ---")
graph2 = [[0, 1, 0], [0, 0, 1], [1, 0, 0]]
print(f"Graph: {graph2}")
result2 = trova_pozzo(graph2)
print(f"Actual Result: {result2}")
print("Expected Result for a pozzo: None\n")


print("--- Test Case 3: Graph with a single node ---")
# A single node knows no one and is known by everyone (vacuously true).
graph3 = [[0]]
print(f"Graph: {graph3}")
result3 = trova_pozzo(graph3)
print(f"Actual Result: {result3}")
print("Expected Result for a pozzo: 0\n")


print("--- Test Case 4: Empty graph ---")
graph4 = []
print(f"Graph: {graph4}")
# Note: Running this on an empty graph might cause an error or unexpected behavior.
# A robust function should ideally handle this case gracefully.
try:
    result4 = trova_pozzo(graph4)
    print(f"Actual Result: {result4}")
except IndexError:
    print("Actual Result: An IndexError occurred.")
print("Expected Result for a pozzo: None\n")


print("--- Test Case 5: Graph with a 'source' node (node 0) ---")
# Node 0 knows everyone, but is not a pozzo.
# This test checks if the function confuses a source with a pozzo.
graph5 = [[0, 1, 1], [0, 0, 0], [0, 0, 0]]
print(f"Graph: {graph5}")
result5 = trova_pozzo(graph5)
print(f"Actual Result: {result5}")
print("Expected Result for a pozzo: None\n")
