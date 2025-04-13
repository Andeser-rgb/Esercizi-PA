from typing import List


# Time complexity
# O(nk)
def solve(n: int, k: int, memo: List[[int]]):
    if memo[n][k] is None:
        if k > n:
            raise ValueError("k can't be greater than n")
        if k < 0:
            raise ValueError("k can't be negative")
        if k == 0:
            memo[n][k] = 1
        elif n == k:
            memo[n][k] = 0
        else:
            memo[n][k] = (k + 1) * solve(n - 1, k, memo) + (n - k) * solve(
                n - 1, k - 1, memo
            )
    return memo[n][k]


def main():
    n = int(input("Inserisci n: "))
    k = int(input("Inserisci k: "))
    memo = [[None for j in range(k + 1)] for i in range(n + 1)]
    print(solve(n, k, memo))
    return


if __name__ == "__main__":
    main()
