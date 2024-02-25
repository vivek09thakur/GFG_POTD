class Solution
{
    public:
    // Complete this function
    long long int count(long long int n)
    {
    	// Your code here
        int coins[] = {3,5,10};
        vector<long> dp(n+1,0);
        dp[0] = 1;
        for(int x:coins){
            for(int j=x;j<=n;j++){
                dp[j] += dp[j-x];
        
            }
        }
        return dp[n];
    	
    }
};
