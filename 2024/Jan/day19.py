class Solution:
    def kTop(self,a, N, K):
        #code here.
        from collections import defaultdict
        ans=[]
        cnt=defaultdict(int)
        lst=[]
        for i,v in enumerate(a):
            cnt[v]+=1
            if cnt[v]==1:
                lst.append(v)
            lst.sort(key=lambda x:(-cnt[x],x))
            ans.append(lst[:min(K,i+1)])
        return ans
