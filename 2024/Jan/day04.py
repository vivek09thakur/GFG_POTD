class Solution:
    def singleElement(self, arr, N):
        # code here 
        return ((sum(set(arr))*3)-sum(arr))//2