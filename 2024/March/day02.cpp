class Solution{
  public:
  int firstElementKTime(int n, int k, int a[]){
    vector<int> vis(201 , 0);
    for(int i = 0 ; i < n ;i++)
    { vis[a[i]]++;if(vis[a[i]] == k) return a[i];}
    return -1;
  }
}
