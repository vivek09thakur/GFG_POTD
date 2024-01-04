class Solution:
    def smallestSubstring(self, s):
        n = len(s)
        res = float('inf')
        prev = [float('-inf')] * 3
        for i in range(n):
            prev[int(s[i])] = i
            res = min(res, i - min(prev) + 1)
        if res == float('inf'):
            return -1
        return res