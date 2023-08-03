"""
Check if an Array is Sorted

Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

Note: Two consecutive equal values are considered to be sorted.
"""
class Solution:

    def bruteforce(self, arr: list) -> bool:
        """
        Time Complexity : O(N)
        Space: O(1)
        """
        for i in range(len(arr)):
            if arr[i] > arr[i+1]:
                return False
        return True