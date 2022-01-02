class Solution:
    def findTwoElement( self,arr, n): 
        i1,i2 = None,None
        for i in range(len(arr)):
            if arr[abs(arr[i]) - 1] < 0:
                i1 = abs(arr[i])
            else:
                arr[abs(arr[i]) - 1] *= -1
        for i in range(len(arr)):
            if arr[i] > 0:i2 = i+1
        return [i1,i2]
