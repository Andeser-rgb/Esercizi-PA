from typing import List


# Complessita O(log n)
# T(n) = T(n) + b
# a = 1, c = 2, k = 0
# a = c^k
def multiply(n: int, a: int):
    if n == 1:
        return a
    res = multiply(n // 2, a + a) 
    if n & 1 == 1:
        res += a


    return res



    

def main():
    sol = multiply(200, 300)
    print(sol)
    return

if __name__ == "__main__":
    main()
