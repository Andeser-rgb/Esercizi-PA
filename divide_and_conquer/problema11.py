from typing import List


# Complessita O(log n)
# T(n) = T(n/2) + b
# a = 1, c = 2, k = 0
def find_turning(a: List[int], s: int, d: int):
    if s == d:
        return s - 1

    m = (s + d) // 2
    res = 0
    if a[m] >= 0:
        res = find_turning(a, s, m)
    else:
        res = find_turning(a, m + 1, d)
    return res



    

def main():
    array = [-5, -3, -1, 2, 4 ,6]
    sol = find_turning(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
