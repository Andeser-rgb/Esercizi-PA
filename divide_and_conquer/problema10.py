from typing import List


# Complessita O(log n)
# T(n) = T(n/2) + b
# a = 1, c = 2, k = 0
def find_zero(a: List[int], s: int, d: int):
    if s == d:
        return s

    m = (s + d) // 2
    res = 0
    if a[m] > 0:
        res = find_zero(a, s, m)
    elif a[m] < 0:
        res = find_zero(a, m + 1, d)
    else:
        res = m
    return res



    

def main():
    array = [-2, -1, 0, 1]
    sol = find_zero(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
