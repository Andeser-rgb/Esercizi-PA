from typing import List


def merge(array: List[int], s: int, m: int, d: int):
    temp = list()
    st = s
    mt = m
    while st < m and mt <= d:
        while st < m and array[st] <= array[mt]:
            temp.append(array[st])
            st += 1
        while mt <= d and st < m and array[mt] <= array[st]:
            temp.append(array[mt])
            mt += 1

    while st < m:
        temp.append(array[st])
        st += 1
    while mt <= d:
        temp.append(array[mt])
        mt += 1

    for i, el in enumerate(temp):
        array[i + s] = el
        
        

# Complessita O(n logn)
# T(n) = 2T(n / 2) + bn
# a = 2, c = 2, k = 1
#
# È possibile risolvere il problema anche con ricerca binaria e iterazione
def contains_product_helper(array: List[int], k: int, s: int, d: int, res: List[[int, int]]):
    if s == d:
        return False
    m = (s + d) // 2
    s1 = contains_product_helper(array, k, s, m, res)
    s2 = contains_product_helper(array, k, m + 1, d, res)
    s3 = False
    if not s1 and not s2:
        l = m
        r = m + 1
        while l >= s and r <= d:
            while  l >= s and k < array[l] * array[r]:
                l -= 1
            if l < s:
                break
            if k == array[l] * array[r]:
                res.append((l, r))
                s3 = True
                break
            while r <= d and k > array[l] * array[r]:
                r += 1
            if r > d:
                break
            if k  == array[l] * array[r]:
                res.append((l, r))
                s3 = True
                break
    #merge(array, s, m + 1, d)

    
    return s1 or s2 or s3
    


def contains_product(array: List[int], k: int, res: List[[int, int]]):
    return contains_product_helper(array, k, 0, len(array) - 1, res)



    

def main():
    array = [2, 3, 5, 7]
    res = list()
    sol = contains_product(array, int(input("Inserisci numero: ")), res)
    print(sol)
    print(res)
    return

if __name__ == "__main__":
    main()
