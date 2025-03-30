from typing import List


# Complessita O(n)
# T(n) = 2T(n/2) + b
# a = 2, c = 2, k = 0
def contains_duplicates(a: List[int], s: int, d: int):
    if s == d:
        return False

    m = int(((s + d) / 2))
    res = a[m] == a[m + 1]
    res |= contains_duplicates(a, s, m)
    res |= contains_duplicates(a, m + 1, d)
    return res



    

def main():
    array = [7, 6, 5, 4, 3, 2, 1, 5]
    array.sort()
    sol = contains_duplicates(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
