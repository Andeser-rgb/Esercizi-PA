from typing import List


# Complessita O(n)
# T(n) = 2T(n/2) + b
# a = 2, c = 2, k = 0
def solve(a: List[int], s: int, d: int):
    if s == d:
        if a[s] >= 0:
            return 1
        else:
            return 0
    c = int((s + d)/2)
    s1 = solve(a, s, c)
    s2 = solve(a, c + 1, d)
    return s1 + s2

    

def main():
    array = [-1, 0, 1, 3, 7, -22, 55, -100, -4523, 21312]
    sol = solve(array, 0, len(array) - 1)
    print(sol)
    return

if __name__ == "__main__":
    main()
