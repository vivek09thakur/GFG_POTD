from typing import List
from itertools import combinations

class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        # code here
        nodes = list(range(1, n+1))
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo)//2
            for perm in combinations(nodes, mid):
                perm = set(perm)
                if all(u in perm or v in perm for u, v in edges):
                    hi = mid
                    break
            else:
                lo = mid + 1
        return lo
