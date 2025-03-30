from typing import List


# Complessita O(log n)
# T(n) = T(n) + b
# a = 1, c = 2, k = 0
# a = c^k
def find_leap(array: List[int], s: int, d: int):
    if s == d:
        return None
    m = (s + d) // 2
    if array[m + 1] - array[m] > 1:
        return m + 1

    if m - s < array[m] - array[s]:
        return find_leap(array, s, m)

    return find_leap(array, m + 1, d)



    

def main():
    array = [0, 2, 3, 4, 5]
    sol = find_leap(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
