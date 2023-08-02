"""
Given two sorted arrays and a number x, find the pair whose sum is closest to x and the pair has an element from each array. 
We are given two arrays ar1[0…m-1] and ar2[0..n-1] and a number x, we need to find the pair ar1[i] + ar2[j] such that absolute value of (ar1[i] + ar2[j] – x) is minimum.
Example: 

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 32      
Output:  1 and 30

Input:  ar1[] = {1, 4, 5, 7};
        ar2[] = {10, 20, 30, 40};
        x = 50      
Output:  7 and 40
"""
import sys


def naive_algo(arr1, arr2, x):
    min_diff = 0
    for index in range(len(arr1)):
        for j in range(len(arr2)):
            val = arr1[index]
            diff = (val + arr2[j] - x)
            print(arr1[index],arr2[j], diff, min_diff)
            if min_diff > diff:
                min_diff = diff
    # print(arr1[index],arr2[j])
    return arr1[index],arr2[j]

def optimization_1(arr1, arr2, x):
    n = len(arr1)
    l,r =0, n-1
    min_diff = sys.maxsize
    res_1, res_2 = 0,0

    while(l<n and r>=0):
        # print(l,r)
        val = arr1[l] + arr2[r]
        # print(abs(val - x) <= min_diff, abs(val - x),min_diff)
        if abs(val - x) <= min_diff:
            res_1, res_2 = l,r
            min_diff = abs(val - x)
        
        if arr1[l+1] + arr2[r] < min_diff:
            l+=1
        else:
            r -= 1
        
        # print(l,r)
        # breakpoint()
    
    return arr1[res_1], arr2[res_2]
        

def main():
    arr1, arr2, x = [1, 4, 5, 7], [10,20,30,40], 50
    
    # Time Space
    # result = naive_algo(arr1, arr2, x)

    # Time Space
    result = optimization_1(arr1, arr2, x)
    
    print(result)
main()