from typing import List
import math


# Complessita O(n)
# T(n) = 2T(n/2) + b
# a = 2, c = 2, k = 0
def solve(a: List[int], l: int, u: int, s: int, d: int):
    assert l < u
    if s == d:
        if a[s] >= l and a[s] <= u:
            return 1
        else:
            return 0

    m = int(((s + d) / 2))
    n1 = solve(a,l,u, s, m)
    n2 = solve(a,l,u, m + 1, d)
    return n1 + n2

    

def main():
    array = [7, 6, 5, 4, 3, 2, 1]
    sol = solve(array, 2, 4, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
