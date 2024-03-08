class Solution{
  public:
    char nthCharacter(string s, int r, int n) {
        //code here
        if(r==0 || n==0)
            return s[n];
        long long j=(1ll<<r);
        int i=n/j;
        n-=(i*j);
        if(s[i]=='1')
            return nthCharacter("10",r-1,n);
        else
            return nthCharacter("01",r-1,n);
        return '2';
    }
};
