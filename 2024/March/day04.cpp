class Solution{
  public:
    void swapElements(int arr[], int n){
        
        // Your code here
         if(n==1 || n==2){
            return;
        }
        
        int i =0, j=i+2;
        while(j<n){
            swap(arr[i], arr[j]);
            i++;
            j++;
        }
    }
};
