class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        factors=[*range(b+1)]
        i=2
        while i*i<=b:
            if factors[i]==i:
                for j in range(i*i,b+1,i):
                    factors[j]=i
            i+=1
        from collections import defaultdict
        ans=0
        for i in range(a,b+1):
            factor=defaultdict(int)
            while i>1:
                factor[factors[i]]+=1
                i//=factors[i]
            ans+=sum(factor.values())
        return ans
