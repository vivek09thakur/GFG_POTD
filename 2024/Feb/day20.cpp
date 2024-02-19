class Solution
{
public:
    int wordBreak(string A, vector<string> &B) {
        int n=A.size();
        if(n==0)
            return 1;
        string temp="";
        for(int i=0;i<n;i++){
            temp.push_back(A[i]);
            if(find(B.begin(),B.end(),temp)!=B.end()){
                string newtemp=A.substr(i+1);
                if(wordBreak(newtemp,B))
                    return 1;
            }
        }
        return 0;
    }
};
