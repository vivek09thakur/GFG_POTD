class Solution:
	def TotalWays(self, N):
		# Code here
		m = 10**9+7
		last_empty , last_occupied = 1,0
		for _ in range(N):
		    last_empty, last_occupied = (last_empty+last_occupied)%m, last_empty
        one_side =(last_empty+last_occupied)%m
        return one_side**2%m
