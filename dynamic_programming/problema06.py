from typing import List


# Time complexity
# O(n^2)
def solve(n: int, costi: List[int], memo: List[int]):
    if n < 0:
        raise ValueError("n non può essere negativo")
    if n == 0:
        return 0
    if memo[n] is None:
        memo[n] = min(
            solve(n - (i + 1), costi, memo) + el
            for i, el in filter(lambda x: n >= x[0] + 1, enumerate(costi))
        )
    return memo[n]


def main():
    costi = [5, 4, 3, 2, 1]
    n = len(costi)
    memo = [None for i in range(n + 1)]
    print(solve(n, costi, memo))
    return


if __name__ == "__main__":
    main()
