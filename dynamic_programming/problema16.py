from typing import List


# Time complexity
# O(n^2)
def solve(x: int, y: int, n: int, map: List[[int]], memo: List[[int]]):
    if x >= n or y >= n:
        return float("-inf")
    if x + 1 == n and y + 1 == n:
        return map[x][y]
    if memo[x][y] is None:
        memo[x][y] = (
            max(solve(x + 1, y, n, map, memo), solve(x, y + 1, n, map, memo))
            + map[x][y]
        )

    return memo[x][y]


def solve_it(map: List[[int]]):
    n = len(map)
    memo = [[None for _ in range(n)] for _ in range(n)]
    memo[0][0] = map[0][0]
    for i in range(1, n):
        memo[0][i] = map[0][i] + memo[0][i - 1]

    for i in range(1, n):
        memo[i][0] = map[i][0] + memo[i - 1][0]

    for i in range(1, n):
        for j in range(1, n):
            memo[i][j] = max(memo[i - 1][j], memo[i][j - 1]) + map[i][j]

    return memo[n - 1][n - 1]


def main():
    grid = [[2, 3], [4, 5]]
    n = len(grid)
    memo = [[None for _ in range(n)] for _ in range(n)]
    print(solve(0, 0, n, grid, memo))
    print(solve_it(grid))
    return 42


if __name__ == "__main__":
    main()
