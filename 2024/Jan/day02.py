class Solution():
    def maxSumWithK(self, a, n, k):
        mn={-1:0}
        ans=-float('inf')
        pfs=a[:]
        for i,v in enumerate(a):
            if i>=1:
                pfs[i]+=pfs[i-1]
            mn[i]=min(mn.get(i-1,float('inf')),pfs[i])
            ans=max(ans,pfs[i]-mn.get(i-k,float('inf')))
        return ans