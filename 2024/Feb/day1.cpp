class Solution
{
  public:
    //Function to check if a string is Pangram or not.
    bool checkPangram (string s) {
        // your code here
        vector<bool> present(26,0);
        for(auto x : s){
            if(isalpha(x)){
                if(islower(x)){
                    int index = x - 'a';
                    present[index] = 1;
                }
                else{
                    int index = x - 'A';
                    present[index] = 1;
                }
            }
        }
        for(auto x : present){
            if(x == 0) return false;
        }
        return true;
    }

};
