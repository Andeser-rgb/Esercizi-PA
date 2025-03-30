from typing import List


def find_min_const(a: List[int], k: int):
    index = (k // len(a) + 1) * len(a) - k
    return a[index]

# Complessita O(log n)
# T(n) = T(n/2) + b
# a = 1, c = 2, k = 0
def find_min_log(a: List[int], s: int, d: int):
    if s == d:
        return a[s]

    m = (s + d) // 2
    res = 0
    if a[m] < a[d]:
        res = find_min_log(a, s, m)
    else:
        res = find_min_log(a, m + 1, d)
    return res



    

def main():
    array = [15, 18, 28, 30, 35, 42, 3, 7]
    min_val = find_min_const(array, 2)
    print(f"Minimum: {min_val}")

    sol = find_min_log(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
