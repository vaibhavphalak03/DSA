class Solution:
    def maxSubArraySum(self, arr):
        res = maxe = arr[0]
        
        for i in range(1, len(arr)):
            
            maxe = max( maxe + arr[i],arr[i] )
            
            res = max(res, maxe)
            
        return res