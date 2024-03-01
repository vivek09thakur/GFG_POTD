class Solution
{
    public:
    int peakElement(int arr[], int n)
    {
       // Your code here
       int max_idx = n-1;
       for(int i = 0; i < n-1; i++){
           if(arr[i] >= arr[i+1]){
               max_idx = i;
               break;
           }
       }
       return max_idx;
    }
};
