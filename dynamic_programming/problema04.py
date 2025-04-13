from typing import List


# Time complexity
# O(n^2)
def solve(n: int, memo: List[int]):
    if n < 0:
        raise ValueError("n cannot be negative")
    if memo[n] is None:
        if n == 0:
            memo[n] = 1
        else:
            memo[n] = sum(solve(i, memo) * solve(n - i - 1, memo) for i in range(n))
    return memo[n]


def main():
    n = int(input("Inserisci n: "))
    memo = [None for i in range(n + 1)]
    print(solve(n, memo))
    return


if __name__ == "__main__":
    main()
