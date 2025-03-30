from typing import List


# Complessita O(n)
# T(n) = 2T(n/2) + b
# a = 2, c = 2, k = 0
def count_mul(a: List[int], s: int, d: int):
    if s == d:
        return 0

    m = int(((s + d) / 2))
    res = 0
    if a[m] * a[m + 1] > 0:
        res += 1
    res += count_mul(a, s, m)
    res += count_mul(a, m + 1, d)
    return res



    

def main():
    array = [7, 6, 5, 4, 3, 2, 1, 5]
    array.sort()
    sol = count_mul(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
