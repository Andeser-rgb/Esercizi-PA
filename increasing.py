from typing import List
import bisect


def longest_increasing_sub(nums: List[int]):
    temp: List[(int, int)] = []
    predecessors = [-1] * len(nums)

    # O(n log n)
    for i, el in enumerate(nums):
        # ricerca binaria posizione in lista temporanea
        ind = bisect.bisect_left(temp, (el, i))  # O(log n)
        if ind == len(temp):
            temp.append((el, i))
        if ind != 0:
            predecessors[i] = temp[ind - 1][1]

        temp[ind] = (el, i)

    solution = []
    last_ind = temp[-1][1]
    while last_ind != -1:
        solution.append(nums[last_ind])
        last_ind = predecessors[last_ind]
    solution.reverse()

    return solution


def main():
    return longest_increasing_sub(
        [
            0,
            8,
            4,
            12,
            2,
            10,
            6,
            14,
            1,
            9,
            5,
            13,
            3,
            11,
            7,
            15,
        ]
    )


if __name__ == "__main__":
    print(main())
