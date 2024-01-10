class Solution:

    def removeKdigits(self, s, k):
        # code here
        n = len(s)
        v = [0] * 10
        st = []
    
        for i in range(n):
            while st and s[i] < st[-1] and k > 0:
                st.pop()
                k -= 1
            if not st and s[i] == '0':
                continue
            st.append(s[i])
    
        while st and k > 0:
            st.pop()
            k -= 1
    
        if not st:
            return "0"
    
        ans = ""
        while st:
            ans += st.pop()
    
        return ans[::-1]
