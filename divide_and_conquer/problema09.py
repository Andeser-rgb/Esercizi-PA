from typing import List


# Complessita O(log n)
# T(n) = T(n/2) + b
# a = 1, c = 2, k = 0
def find_shift(a: List[int], s: int, d: int):
    if s == d:
        return len(a) - s

    m = (s + d) // 2
    res = 0
    if a[m] < a[d]:
        res = find_shift(a, s, m)
    else:
        res = find_shift(a, m + 1, d)
    return res



    

def main():
    array = [30, 35, 42, 1, 7, 15, 18, 28]
    sol = find_shift(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
