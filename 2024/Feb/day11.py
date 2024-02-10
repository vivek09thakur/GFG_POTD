class Solution:
    def recamanSequence(self, n):
        # code here
        arr =[0] * n
        lst=set([0])
        if n>0:
            for i in range(1,n):
                arr[i]=arr[i-1]-i
                if arr[i]<0 or (arr[i] in lst):
                    arr[i]=arr[i-1]+i
                lst.add(arr[i])
        return arr
