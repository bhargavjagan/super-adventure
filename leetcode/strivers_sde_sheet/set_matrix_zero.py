"""
https://leetcode.com/problems/set-matrix-zeroes/description/

Question:
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place. - so do it in the same matrix

Example:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Constraints:

    m == matrix.length
    n == matrix[0].length
    1 <= m, n <= 200
    -231 <= matrix[i][j] <= 231 - 1

Follow up:
- A straightforward solution using O(mn) space is probably a bad idea.
- A simple improvement uses O(m + n) space, but still not the best solution.
- Could you devise a constant space solution? 
"""
from types import ClassMethodDescriptorType
from typing import List
import time

class Solution:

    @classmethod
    def bruteForce(cls, matrix: List[List[int]]) -> List[List[int]]:
        """
        A burteforce solution for the problem.
        Time: O(m*n)
        Space: O(m*n)
        """
        zero_positions = set() # O(m*n)
        rows, columns = len(matrix), len(matrix[0]) #O(1)
        for row_index in range(rows): #O(m*n)
            for column_index in range(columns):
                if matrix[row_index][column_index] == 0:
                    zero_positions.add((row_index, column_index))

        if zero_positions:
            zero_rows = [0 for i in range(columns)] #O(m)
            for r, c in zero_positions: #O(m*n)
                matrix[r] = zero_rows # replace the rows with zeros O(1)
                for row in matrix: # replace the columns with zero O(m)
                    row[c] = 0
        
        return matrix

    @classmethod
    def betterSolution(cls, matrix:List[List[int]]) -> List[List[int]]:
        m = len(matrix[0])
        n = len(matrix)
        column_flag = [0] * m
        rows_flag = [0] * n

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    column_flag[j] = 1
                    rows_flag[i] = 1

        for i in range(n):
            for j in range(m):
                if rows_flag[i] or column_flag[j]:
                    matrix[i][j] = 0

        return matrix
    
    @classmethod
    def optimal_solution(cls, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix) #rows
        m = len(matrix[0]) # columns
        col0 = 1

        # traverse and mark all of the zeros
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    #mark the row
                    matrix[i][0] = 0

                    #mark the column
                    if j != 0: 
                        matrix[0][j] = 0
                    else:
                        col0 = 0
        
        # traverse from the bottom and make them zeros
        for i in range(1, n):
            for j in range(1, m):
                if matrix[i][j] != 0:
                    if matrix[0][j] or matrix[i][0]:
                        matrix[i][j] = 0
    
        # check for the edge cases
        if matrix[0][0] == 0:
            matrix[0] = [0 for _ in range(m)]

        if col0 == 0:
            for i in range(n):
                matrix[i][0] = 0

        return matrix


    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.bruteForce(matrix)
        print(matrix)
 
if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    solution = [[1,0,1],[0,0,0],[1,0,1]]

    start_time = time.time()
    output = Solution.bruteForce(matrix)
    assert output == solution
    print(time.time() - start_time, "ms")
    