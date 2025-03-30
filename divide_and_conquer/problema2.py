from typing import List
import math


# Complessita O(n)
# T(n) = 2T(n/2) + b
# a = 2, c = 2, k = 0
def solve(a: List[int], s: int, d: int):
    if s == d:
        return (0, a[s], a[s])
    m = int(((s + d) / 2))
    (s1, min1, max1) = solve(a, s, m)
    (s2, min2, max2) = solve(a, m + 1, d)
    min_num = min(min1, min2)
    max_num = max(max1, max2)
    return (min(min2 - max1, s1, s2), min_num, max_num)

    

def main():
    array = [7, 6, 5, 4, 3, 2, 1]
    sol = solve(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
