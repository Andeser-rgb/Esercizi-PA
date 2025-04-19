from typing import List


x = 4
y = 2
z = 5


# Time complexity
# O(n^2)
def solve(a: str, s: int, d: int, memo: List[[int]]):
    if s >= d:
        return 0
    if memo[s][d] is None:
        if a[s] == a[d]:
            memo[s][d] = solve(a, s + 1, d - 1, memo)
        else:
            memo[s][d] = min(
                solve(a, s, d - 1, memo) + x,
                solve(a, s, d - 1, memo) + y,
                solve(a, s + 1, d, memo) + x,
                solve(a, s + 1, d, memo) + y,
                solve(a, s + 1, d - 1, memo) + z,
            )
    return memo[s][d]


def main():
    a = input("Inserisci stringa: ")
    n = len(a)
    memo = [[None for j in range(n)] for i in range(n)]
    print(solve(a, 0, n - 1, memo))
    return


if __name__ == "__main__":
    main()
