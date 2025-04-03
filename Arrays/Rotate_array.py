class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        #for i in range(d):
           # temp = arr.pop(0)
          #  arr.append(temp)
            
            
        n = len(arr)
        
        d%=n
        #reverse the first d element
        reverse(arr, 0 , d-1)
        
        #reverse the remaining n-d element
        reverse(arr, d, n-1)
        
        #reverse the entire array
        reverse(arr, 0 , n-1)



def reverse(arr,start,end):
    while start < end:
        arr[start] , arr[end] = arr[end], arr[start]
        
        start+=1
        end-=1
