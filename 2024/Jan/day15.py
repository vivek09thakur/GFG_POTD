from typing import List


class Solution:
    def max_courses(self, n : int, total : int, cost : List[int]) -> int:
        import sys
        sys.setrecursionlimit(3*10**3)
        import math
        from functools import lru_cache
        @lru_cache(None)
        def dp(i=0,tot=total):
            nonlocal cost,n
            if i>=n or tot==0:
                return 0
            mx=dp(i+1,tot)
            if tot>=cost[i]:
                mx=max(mx,dp(i+1,tot-cost[i]+math.floor(cost[i]*.9))+1)
            return mx
        return dp()
