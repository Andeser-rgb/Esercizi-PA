from typing import List


# Time complexity
# O(nk)
def solve(i: int, j: int, memo: List[[int]]):
    if i < 0 or j < 0:
        raise ValueError("i and j can't be negative")
    if memo[i][j] is None:
        if i == 0 or j == 0:
            memo[i][j] = 1
        else:
            memo[i][j] = i * solve(i - 1, j, memo) + (i + j) * solve(i - 1, j - 1, memo)
    return memo[i][j]


def main():
    n = int(input("Inserisci n: "))
    k = int(input("Inserisci k: "))
    memo = [[None for j in range(k + 1)] for i in range(n + 1)]
    print(solve(n, k, memo))
    return


if __name__ == "__main__":
    main()
