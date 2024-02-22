class Solution
{
    public:
    const int mod=1e9+7;
    int solve(int i,int j, int n, int m, string s, string t, vector<vector<int>>&dp){
        if(j==m)return 1;
        if(i==n)return 0;
        if(dp[i][j]!=-1)return dp[i][j];
        int ans=solve(i+1,j,n,m,s,t,dp);
        if(s[i]==t[j]){
            ans=(ans+solve(i+1,j+1,n,m,s,t,dp));
        }
        dp[i][j]=ans%mod;
        return dp[i][j];
    }
    int subsequenceCount(string s, string t)
    {
      //Your code here
      int n=s.length();
      int m=t.length();
      vector<vector<int>>dp(n+1,vector<int>(m+1,-1));
      return solve(0,0,n,m,s,t,dp);
    }
};
