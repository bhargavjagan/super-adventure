class Solution:

    def bruteforce(self, arr: list) -> int:
        """
        Time : O(N)
        Space: O(1)
        """
        maximum = arr[0]
        for i in arr:
            if i> maximum:
                maximum = i
        return maximum
    
"""
Find Second Smallest and Second Largest Element in an array

Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
"""
class SmallestSolution:

    def bruteforce(self, arr: list) -> tuple[int, int]:
        """
        Time: O(n* log N)
        Spave: O(1)
        """
        if len(arr) < 2:
            # nothing to compare, so -1
            return -1
        
        arr.sort()  
        print(arr[1], arr[-2])     

class LeftRotate:
    def bruteforce(self, arr: list ) -> int:
        if arr:
            arr.append(arr.pop(0))
            
        return arr

