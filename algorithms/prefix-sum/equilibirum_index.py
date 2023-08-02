"""
Given a sequence arr[] of size n, Write a function int equilibrium(int[] arr, int n) that returns an equilibrium index (if any) or -1 if no equilibrium index exists. 

The equilibrium index of an array is an index such that the sum of elements at lower indexes is equal to the sum of elements at higher indexes. 

Input: A[] = {-7, 1, 5, 2, -4, 3, 0} 
Output: 3 
3 is an equilibrium index, because: 
A[0] + A[1] + A[2] = A[4] + A[5] + A[6]

Input: A[] = {1, 2, 3} 
Output: -1 

"""

from turtle import right


def naive_algo(arr: list) -> int:
    result = -1
    n = len(arr)
   
    for index in range(1, n + 1):
        if sum(arr[:index]) == sum(arr[index + 1:]):
            return index
    return result

def optimization_1(arr: list) -> list:
    total_sum = sum(arr)

    right_sum = 0
    for index in range(len(arr)):
        total_sum -= arr[index]
        print(total_sum, right_sum)
        if right_sum == total_sum:
            return index
        right_sum += arr[index]
    return -1  

def optimization_2(arr: list) -> int:
    right_arr = []
    left_arr = []

    for i in range(len(arr)):

        if(i):
            left_arr.append(left_arr[i-1]+arr[i])
            right_arr.append(right_arr[i-1]+arr[len(arr)-1-i])
        else:
            left_arr.append(arr[i])
            right_arr.append(arr[len(arr)-1])

    for i in range(len(arr)):
        if(left_arr[i] == right_arr[len(arr)- 1- i]):
            return (i)
    return -1
def main():
    arr = [[-7, 1, 5, 2, -4, 3, 0], [1, 2, 3]]
    for input in arr:
        # Time O(N*2), Space O(1)
        # print("Result: ", naive_algo(input))

        # Time O(N), Space O(1)
        # print("Result: ", optimization_1(input))

        # Time O(N), Space O(N)
        print("Result: ", optimization_2(input))
    
main()