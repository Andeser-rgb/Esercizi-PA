from typing import List


        

# Complessita O(logn)
# T(n) = T(n / 2) + b
# a = 1, c = 2, k = 0
def find_relative_max_helper(array: List[int],  s: int, d: int):
    if s == d:
        return s
    m = (s + d) // 2
    if array[s] > array[m]:
        return find_relative_max_helper(array, s, m)

    return find_relative_max_helper(array, m + 1, d)

    


# Input: array a=a[1]...a[n] tale che a[1] > a[n]
# Output: Indice i tale che a[i] < a[i - 1]
def find_relative_max(array: List[int]):
    return find_relative_max_helper(array, 0, len(array) - 1)



    

def main():
    array = [3, 4, 2]
    res = list()
    sol = find_relative_max(array)
    print(sol)
    return

if __name__ == "__main__":
    main()
