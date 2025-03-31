from typing import List


# Complessita O(logn)
# T(n) = T(n / 2) + b
# a = 1, c = 2, k = 0
def find_rel_min_helper(array: List[int], s: int, d: int):
    if s == d:
        return array[s]

    m = (s + d) // 2

    if (array[m] <= array[m + 1]) and (m == s or array[m] <= array[m - 1]):
        return array[m]

    if array[m] >= array[m + 1]:
        return find_rel_min_helper(array, m + 1, d)

    return find_rel_min_helper(array, s, m)


# O(sqrt(n))
# T(n) = 2T(n/2) + bn^(1/2)
# a = 2, c = 2, k = 1/2
def find_rel_min(array: List[int]):
    return find_rel_min_helper(array, 0, len(array) - 1)


def main():
    array = [1, 2, 3]
    sol = find_rel_min(array)
    print(sol)
    return


if __name__ == "__main__":
    main()
