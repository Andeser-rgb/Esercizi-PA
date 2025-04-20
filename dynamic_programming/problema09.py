from typing import List


# Time complexity
# O(n^2)
def solve(n: int, p: List[int], memo: List[int]):
    if n == 0:
        return 0
    if memo[n] is None:
        memo[n] = max(solve(n - i, p, memo) + el for i, el in enumerate(p[:n], 1))

    return memo[n]


def main():
    a = list(map(lambda x: int(x), input("Inserisci pesi: ").split(" ")))
    n = len(a)
    memo = [None for i in range(n + 1)]
    print(solve(n, a, memo))
    return


if __name__ == "__main__":
    main()
