'''
Given an array of integers arr[] in a circular fashion. Find the maximum subarray sum that we can get if we assume the array to be circular.

Examples:

Input: arr[] = [8, -8, 9, -9, 10, -11, 12]
Output: 22
Explanation: Starting from the last element of the array, i.e, 12, and moving in a circular fashion, we have max subarray as 12, 8, -8, 9, -9, 10, which gives maximum sum as 22.
Input: arr[] = [10, -3, -4, 7, 6, 5, -4, -1]
Output: 23
Explanation: Maximum sum of the circular subarray is 23. The subarray is [7, 6, 5, -4, -1, 10].
Input: arr[] = [-1, 40, -14, 7, 6, 5, -4, -1] 
Output: 52
Explanation: Circular Subarray [7, 6, 5, -4, -1, -1, 40] has the maximum sum, which is 52.
Constraints:
1 <= arr.size() <= 105
-104 <= arr[i] <= 104
'''


def circularSubarraySum(arr):

    totalsum = 0
    currmaxsum = 0
    currminsum = 0
    maxsum = arr[0]
    minsum = arr[0]
    
    for i in range(len(arr)):
        
        currmaxsum = max(currmaxsum + arr[i],arr[i])
        maxsum = max(maxsum , currmaxsum)
        
        currminsum = min(currminsum + arr[i],arr[i])
        minsum = min(minsum , currminsum)
        
        
        totalsum += arr[i]
        
    normalsum = maxsum 
    circularsum = totalsum - minsum
    
    
    if minsum == totalsum:
        return normalsum
        
    return max(normalsum,circularsum)