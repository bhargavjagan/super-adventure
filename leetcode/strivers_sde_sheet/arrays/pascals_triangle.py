"""
Variation 1: Given row number r and column number c. Print the element at position (r, c) in Pascal’s triangle.

Variation 2: Given the row number n. Print the n-th row of Pascal’s triangle.

Variation 3: Given the number of rows n. Print the first n rows of Pascal’s triangle.
"""

class Solution:
    # variation 1
    @classmethod
    def factorial(cls, n: int) -> int:
        if n ==0 or n==1:
            return 1
        else:
            return n * cls.factorial(n-1)
        
    @classmethod
    def nCr(cls, n: int, r: int) -> int:
        res = 1
        for i in range(r):
            res = res * (n -  i)
            res = res // (i+1)
        return res
    
    def var1_bruteforce(self, r: int, c: int) -> int:
        if (c>r):
            return -1
        return int(self.factorial(r-1) / (self.factorial(r-c) * self.factorial(c-1)))

    def var1_optimization_1(self, r: int, c: int) -> int:
        if (c>r):
            return -1
        return self.nCr(r-1,c-1)
    
    @staticmethod
    def generateRow(n: int) -> int:
        res = 1
        arr = [1]
        for i in range(1, n):
            res = res * (n-i)
            res = res // i
            arr.append(int(res))
        return arr
    
    def var3_optimization(self, n: int) -> int:
        arr = []
        for i in range(1, n +1):
            arr.append(self.generateRow(i))
        return arr

if __name__ == "__main__":
    # test the factorial
    values = [(0,1),(1,1),(2,2),(3,6)]
    for i,j in values:
        assert Solution.factorial(i) == j

    samples = [(1,2,-1), (2,1,1), (3,2,2)]
    for r,c,out in samples:
        assert Solution().var1_bruteforce(r,c) == out
        assert Solution().var1_optimization_1(r,c) == out

    samples = [(1, [1]), (2, [1, 1]), (3, [1,2,1]), (4, [1,3,3,1])]
    for n, out in samples:
        assert out in Solution().var3_optimization(n)
