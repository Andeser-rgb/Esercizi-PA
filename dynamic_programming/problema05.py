from typing import List


# Time complexity
# O(n)
def solve(n: int, memo: List[int]):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if memo[n] is None:
        memo[n] = solve(n - 1, memo) + solve(n - 3, memo) + solve(n - 4, memo)
    return memo[n]


def main():
    n = int(input("Inserisci n: "))
    memo = [None for i in range(n + 1)]
    print(solve(n, memo))
    return


if __name__ == "__main__":
    main()
