from typing import List


# Time complexity
# O(Tk)
def solve(t: int, a_index: int, a: List[int], memo: List[[int]]):
    if a_index < 0:
        return False
    if t == a[a_index]:
        return True
    if memo[t][a_index] is None:
        memo[t][a_index] = solve(t, a_index - 1, a, memo)
        if t % a[a_index] == 0:
            memo[t][a_index] |= solve(t // a[a_index], a_index - 1, a, memo)

    return memo[t][a_index]


def main():
    t = int(input("Inserisci T: "))
    a = list(map(lambda x: int(x), input("Inserisci A: ").split(" ")))
    memo = [[None for i in range(len(a))] for _ in range(t + 1)]
    print(solve(t, len(a) - 1, a, memo))
    return


if __name__ == "__main__":
    main()
