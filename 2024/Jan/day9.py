class Solution:
    def search(self, pat, txt):
        # code here
        ind = []
        res = []
        for i in range(len(txt)):
            if txt[i]==pat[0]:
                ind.append(i)
        for i in ind:
            if i+len(pat)<=len(txt) and txt[i:i+len(pat)]== pat:
                res.append(i+1)
        return res
