from typing import List


x = 4
y = 2
z = 5


# Time complexity
# O(Cn)
def solve(crediti: int, d: List[int], c: List[int], e_ind: int, memo: List[[int]]):
    if crediti <= 0:
        return 0
    if e_ind < 0:
        return float("-inf")
    if memo[crediti][e_ind] is None:
        memo[crediti][e_ind] = min(
            solve(crediti, d, c, e_ind - 1, memo),
            solve(crediti - c[e_ind], d, c, e_ind - 1, memo) + d[e_ind],
        )

    return memo[crediti][e_ind]


def main():
    difficolta = list(map(lambda x: int(x), input("Inserisci difficoltà: ").split(" ")))
    crediti = list(map(lambda x: int(x), input("Inserisci crediti: ").split(" ")))
    crediti_totali = int(input("Inserisci crediti totali: "))
    n = len(crediti)
    memo = [[None for i in range(n + 1)] for _ in range(crediti_totali + 1)]
    print(solve(crediti_totali, difficolta, crediti, n - 1, memo))
    return


if __name__ == "__main__":
    main()
