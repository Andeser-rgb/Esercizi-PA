from typing import List
import math


# Complessita O(log n)
# T(n) = T(n/2) + b
# a = 1, c = 2, k = 0
def least_bigger(a: List[int], x: int, s: int, d: int):
    if s == d:
        if a[s] > x:
            return s
        else:
            return None

    m = int(((s + d) / 2))
    res = 0
    if a[m] > x:
        res = least_bigger(a, x, s, m)
    else:
        res = least_bigger(a, x, m + 1, d)
    return res

# Complessita O(log n)
# T(n) = O(log n) + O(log n)
def solve(a: List[int], l: int, u: int):
    assert l < u
    n1 = least_bigger(a, l - 1, 0, len(a) - 1)
    n2 = least_bigger(a, u, 0, len(a) - 1)
    if n1 is None:
        n1 = len(a)
    if n2 is None:
        n2 = len(a)
    return n2 - n1


    

def main():
    array = [7, 6, 5, 4, 3, 2, 1]
    array.sort()
    sol = solve(array, 4, 8)
    print(sol)
    return

if __name__ == "__main__":
    main()
