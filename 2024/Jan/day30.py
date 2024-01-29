class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        def rec(n1,n2,n3):
            if n1<=0 or n2<=0 or n3<=0:
                return 0
            if (n1,n2,n3) not in dp:
                if A[n1-1]==B[n2-1] and B[n2-1]==C[n3-1]:
                    ans=1+rec(n1-1,n2-1,n3-1)
                else:
                    ans=max(rec(n1,n2-1,n3-1),rec(n1-1,n2,n3-1),rec(n1-1,n2-1,n3),rec(n1,n2,n3-1),rec(n1-1,n2,n3),rec(n1,n2-1,n3))
                dp[(n1,n2,n3)]=ans
            return dp[(n1,n2,n3)]
        dp=dict()
        return  rec(n1,n2,n3)
