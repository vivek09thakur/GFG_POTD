class Solution:
    def sequence(self, n):
        # code here
        M = 10**9+7
        ans = 0
        start = 1
        for i in range(1,n+1):
            v = 1
            while i > 0:
                v = v*start%M
                start += 1
                i -= 1
            ans = (ans+v)%M
        return ans
