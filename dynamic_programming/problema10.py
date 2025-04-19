from typing import List


x = 4
y = 2
z = 5


# Time complexity
# O(Cn)
def solve(crediti: int, d: List[int], c: List[int], memo: List[int]):
    if crediti <= 0:
        return 0
    if memo[crediti] is None:
        memo[crediti] = min(
            solve(crediti - el, d, c, memo) + d[i] for i, el in enumerate(c)
        )

    return memo[crediti]


def main():
    difficolta = list(map(lambda x: int(x), input("Inserisci difficoltà: ").split(" ")))
    crediti = list(map(lambda x: int(x), input("Inserisci crediti: ").split(" ")))
    crediti_totali = int(input("Inserisci crediti totali: "))
    n = len(crediti)
    memo = [None for i in range(n + 1)]
    print(solve(n, crediti, memo))
    return


if __name__ == "__main__":
    main()
