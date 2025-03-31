from typing import List
import math


# Complessita O(log n)
# T(n) = T(n/2) + b
# a = 1, c = 2, k = 0
def solve(a: List[int], x: int, s: int, d: int):
    if s == d:
        if a[s] > x:
            return s
        else:
            return None

    m = int(((s + d) / 2))
    res = 0
    if a[m] > x:
        res = solve(a, x, s, m)
    else:
        res = solve(a, x, m + 1, d)
    return res

    

def main():
    array = [7, 6, 5, 4, 3, 2, 1]
    array.sort()
    sol = solve(array, 2, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
