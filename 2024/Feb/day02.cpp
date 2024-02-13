class Solution{
  public:
    /*You are required to complete this method */
    int atoi(string s) {
        //Your code here
        string ch="qwertyuiopasdfghjklzxcvbnm";
        string minus="-";
        for(int i=0;i<s.size();i++){
            if(ch.find(s[i])!=string::npos){
                return -1;
            }
            if(minus.find(s[i])!=string::npos && i!=0){
                return -1;
            }
        }
        int ans=stoi(s);
        return ans;
    }
};
