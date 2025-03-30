from typing import List


# Complessita O(n)
def find_el_helper(array: List[List[int]], k: int, row: int, col: int):
    if row >= len(array) or col < 0:
        return None
    if array[row][col] == k:
        return (row, col)
    if array[row][col] > k:
        return find_el_helper(array, k, row + 1, col)
    return find_el_helper(array, k, row, col - 1)
    


def find_el(array: List[List[int]], k: int):
    return find_el_helper(array, k, 0, len(array[0]) - 1)



    

def main():
    array = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1],
    ]
    sol = find_el(array, int(input("Inserisci numero: ")))
    print(sol)
    return

if __name__ == "__main__":
    main()
