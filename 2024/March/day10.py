class Solution:

	def removeDuplicates(self,st):
	    # code here
	    s = set()
	    ans = ''
	    for i in range(len(st)):
	        if st[i] not in s:
	            s.add(st[i])
	            ans += st[i]
	    return ans
