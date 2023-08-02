"""
Given an array of positive and negative numbers, the task is to find if there is a subarray (of size at least one) with 0 sum.

Input: {4, 2, -3, 1, 6}
Output: true 
Explanation:
There is a subarray with zero sum from index 1 to 3.

Input: {4, 2, 0, 1, 6}
Output: true
Explanation: The third element is zero. A single element is also a sub-array.

"""
def naive_algo(arr) -> bool:
    for index in range(len(arr)):
        if arr[index] == 0:
            print(arr[index])
            return True
        
        sum = 0

        for j in range(index,len(arr)):
            sum += arr[j]
            if sum == 0:
                print(arr[index:j + 1])
                return True
    
    return False

def optimization_1(arr: list) -> bool:
    """
    if there is a sub array that has the zero sum, then the value before
    the sub-array Ai and after the sub - array Aj must hold the same sum value.
    """
    sum_array = set()
    sum_val = 0
    for index in range(len(arr)):
        sum_val += arr[index]
        sum_array.add(sum_val)

        if arr[index] == 0 or sum_val in sum_array[:-1]:
            return True

    return False

def main():
    arr = [[4, 2, -3, 1, 6], [4, 2, 0, 1, 6],[0, 1],[-3, 2, 3, 1, 6]]
    for a in arr:
        # Time: O(N*2) Space : O(1)
        # print(naive_algo(a))

        # Time: O(N) Space : O(1)
        print(optimization_1(a))

main()