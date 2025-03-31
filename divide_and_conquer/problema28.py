from typing import List
from math import ceil


def find_subsequence(a: str, b: str, k: int):
    i = 0
    j = 0
    rep = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            rep += 1
        i += 1
        if rep == k:
            j += 1
            rep = 0
    return j == len(b)


# Complessita O(nlogn)
# T(n) = T(n / 2) + bn0
# a = 1, c = 2, k = 1
def find_max_subsequence_helper(a: str, b: str, s: int, d: int):
    if s == d:
        return s

    m = ceil((s + d) / 2)

    if find_subsequence(a, b, m):
        return find_max_subsequence_helper(a, b, m, d)
    return find_max_subsequence_helper(a, b, s, m - 1)


def find_max_subsequence(a: str, b: str):
    max_k = len(a) // len(b)
    return find_max_subsequence_helper(a, b, 0, max_k)


def main():
    sol = find_max_subsequence("abababababac", "abc")
    print(sol)
    return


if __name__ == "__main__":
    main()
