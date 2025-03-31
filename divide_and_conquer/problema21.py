from typing import List


# Complessita O(logn)
# T(n) = T(n / 2) + b
# a = 1, c = 2, k = 0
def find_double_helper(array: List[int], s: int, d: int):
    if s == d:
        return None

    m = (s + d) // 2

    if array[m] == array[m + 1]:
        return array[m]

    if array[m] - array[s] == m - s:
        return find_double_helper(array, m + 1, d)

    return find_double_helper(array, s, m)


# Input: array a=a[1]...a[n] tale che a[1] > a[n]
# Output: Indice i tale che a[i] < a[i - 1]
def find_double(array: List[int]):
    return find_double_helper(array, 0, len(array) - 1)


def main():
    array = [1, 2, 2]
    sol = find_double(array)
    print(sol)
    return


if __name__ == "__main__":
    main()
