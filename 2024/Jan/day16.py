class Solution:
    def numberSequence(self, m, n):
        from functools import lru_cache
        @lru_cache(None)
        def dp(sto=m,cnt=n):
            if sto==0:
                return int(cnt==0)
            return dp(sto//2,cnt-1)+dp(sto-1,cnt)
        return dp()
