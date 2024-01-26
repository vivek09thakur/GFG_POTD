class Solution{
public:
    string matrixChainOrder(int arr[], int n){
        // code here
        n--;
        vector<vector<int>> dp(n,vector<int>(n,1000000000));
       
        vector<vector<string>> ans(n,vector<string>(n,""));
        for(int len=1;len<n+1;len++)
        {
            for(int i=0;i+len<=n;i++)
            {
                if(len==1)
                {dp[i][i]=0;
                ans[i][i]=char('A'+i);
                }
                for(int j=i;j<i+len-1;j++)
                {
                    if(dp[i][i+len-1]>dp[i][j]+arr[i]*arr[j+1]*arr[len+i]+dp[j+1][len+i-1])
                    {
                    dp[i][i+len-1]=dp[i][j]+arr[i]*arr[j+1]*arr[len+i]+dp[j+1][len+i-1];
                    ans[i][i+len-1]="("+ans[i][j]+ans[j+1][len+i-1]+")";
                    }
                }
            }
        }
        return ans[0][n-1];
        
    }
};