
class Solution{
  public:	
	
	int countPairs(vector<vector<int>> &mat1, vector<vector<int>> &mat2, int n, int x){
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            mat1[i][j]=x-mat1[i][j];
        }
        reverse(mat1[i].begin(),mat1[i].end());
    }
    reverse(mat1.begin(),mat1.end());
    int i1=0,j1=0,i2=0,j2=0;
    int ans = 0;
    while(i1<n & i2<n){
        if(mat1[i1][j1]<mat2[i2][j2]){
            j1++;
            if(j1==n)i1++,j1=0;
        }
        else if(mat1[i1][j1]>mat2[i2][j2]){
            j2++;
            if(j2==n)i2++,j2=0;
        }
        else{
            ans++;
            j1++,j2++;
            if(j1==n)i1++,j1=0;
            if(j2==n)i2++,j2=0;
        }
    }
    return ans;
  }
};
