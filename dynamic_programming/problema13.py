from typing import List


x = 4
y = 2
z = 5


# Time complexity
# O(Cn)
def solve(x: int, y: int, n: int, memo: List[[int]]):
    if x == n and y == n:
        return 1
    if x > n or y > n:
        return 0
    if memo[x][y] is None:
        memo[x][y] = solve(x + 1, y, n, memo) + solve(x, y + 1, n, memo)

    return memo[x][y]


def main():
    n = int(input("Inserisci n: "))
    memo = [[None for i in range(n + 1)] for _ in range(n + 1)]
    print(solve(0, 0, n - 1, memo))
    return


if __name__ == "__main__":
    main()
