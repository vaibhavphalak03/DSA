'''
Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.

You need to solve this problem without utilizing the built-in sort function.

Examples:

Input: arr[] = [0, 1, 2, 0, 1, 2]
Output: [0, 0, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.
Input: arr[] = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
Output: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
Explanation: 0s 1s and 2s are segregated into ascending order.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?
Constraints:
1 <= arr.size() <= 106
0 <= arr[i] <= 2

'''

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n = len(arr)
        lo = 0
        hi = n - 1
        mid = 0
        
        
        while mid <= hi:
            if arr[mid] == 0:
                arr[lo], arr[mid] = arr[mid], arr[lo]
                lo = lo + 1
                mid = mid + 1
                
            elif arr[mid] == 1:
                mid = mid + 1
                
            else:
                arr[mid], arr[hi] = arr[hi], arr[mid]
                hi = hi - 1
                
        return arr