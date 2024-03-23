class Solution:
    mod = 10**9+7
    def series(self, n):
        # Code here
        ans = [0,1]
        for i in range(n-1):
            ans.append((ans[-1] + ans[-2])%self.mod)
        return ans if n else [0]
