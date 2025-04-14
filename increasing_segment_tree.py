from typing import List
import bisect


def next_power_of_two(n: int):
    if n < 0:
        return ValueError("Input must be non-negative")
    if n == 0:
        return 1
    return 1 << n.bit_length()


class SegmentTree:
    def __init__(self, array: List[int]):
        n = next_power_of_two(len(array))
        tree = [(0, 0)] * (2 * n)
        for i in range(0, len(array)):
            tree[i + n] = (array[i], i)

        k = n // 2
        while k > 0:
            for i in range(k, 2 * k):
                tree[i] = max(tree[2 * i], tree[2 * i + 1])
            k //= 2

        self.tree = tree
        self.len = len(array)

    def update(self, k: int, x: (int, int)):
        n = len(self.tree) // 2
        k += n

        self.tree[k] = x
        k //= 2
        while k > 0:
            self.tree[k] = max(self.tree[2 * k], self.tree[2 * k + 1])
            k //= 2

    def max(self, a: int, b: int):
        n = len(self.tree) // 2
        a += n
        b += n
        res = (0, 0)
        while a <= b:
            if a % 2 == 1:
                res = max(res, self.tree[a])
                a += 1
            if b % 2 == 0:
                res = max(res, self.tree[b])
                b -= 1
            a //= 2
            b //= 2
        return res


def longest_increasing_sub_segment_tree(nums: List[int]):
    if not nums:
        return []

    # Lista utilizzata per ricostruire la sottosequenza
    predecessors = [-1] * (len(nums) + 1)

    # Compressione dei valori della lista in indici da 0 ad N - 1
    index_compression = list(map(lambda x: (x[1], x[0]), enumerate(nums.copy())))
    index_compression.sort()

    # Inizializzazione segment tree (I valori dell'array orignale verranno rappresentati nel range [1, N] mentre il valore all'indice 0 del segment tree sarà pari a 0)
    seg_tree = SegmentTree([0] * (len(nums) + 1))

    lis_len = 0
    lis_end = 0

    # O(n log n)
    for i, el in enumerate(nums):
        # Conversione del valore dell'array in indice "compresso" con ricerca binaria
        ind = bisect.bisect_left(index_compression, (el, i)) + 1  # O(log n)

        (prev_lis, prev_ind) = seg_tree.max(0, ind - 1)  # O(log n)
        predecessors[ind] = prev_ind
        seg_tree.update(ind, (prev_lis + 1, ind))  # O(log n)

        if (prev_lis + 1) > lis_len:
            lis_len = prev_lis + 1
            lis_end = ind

    # Costruzione sottosequenza O(n)
    solution = list()
    while predecessors[lis_end] != -1:
        solution.append(index_compression[lis_end - 1][0])
        lis_end = predecessors[lis_end]
    solution.reverse()

    return solution


def main():
    return longest_increasing_sub_segment_tree(
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
