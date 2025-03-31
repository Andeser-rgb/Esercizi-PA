from typing import List


        

# Complessita O(logn)
# T(n) = T(n / 2) + b
# a = 1, c = 2, k = 0
def find_last_occurrence_helper(array: List[int], x:int,   s: int, d: int):
    if s == d:
        if array[s] == x:
            return s
        else:
            return -1

    m = (s + d) // 2
    if array[m] == x:
        if array[m + 1] == x:
            return find_last_occurrence_helper(array, x, m + 1, d)
        else:
            return m
    if array[m] > x:
        return find_last_occurrence_helper(array,x, s, m)

    return find_last_occurrence_helper(array,x, m + 1, d)

    


# Input: array a=a[1]...a[n] tale che a[1] > a[n]
# Output: Indice i tale che a[i] < a[i - 1]
def find_last_occurence(array: List[int], x: int):
    return find_last_occurrence_helper(array, x,  0, len(array) - 1)



    

def main():
    array = [2, 2, 3, 3, 3,4, 4, 5, 6, 6, 6, 7]
    sol = find_last_occurence(array, int(input("Inserisci numero: ")))
    print(sol)
    return

if __name__ == "__main__":
    main()
