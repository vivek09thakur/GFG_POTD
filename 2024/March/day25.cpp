class Solution{
public:
    vector<string>v;
    void f(int n , string s){
        if(n == 0){
            int cnt = 0;
            for(int i = 0 ; i < s.size(); i++){
                if(s[i] == '1'){
                    cnt++;
                }
                else {
                    cnt--;
                }
                if(cnt < 0){
                    break;
                }
            }
            if(cnt >= 0){
            v.push_back(s);
            }
            return ;
        }
        s.push_back('0');
        f(n-1,s);
        s.pop_back();
        s.push_back('1');
        f(n-1,s);
        s.pop_back();
    }
vector<string> NBitBinary(int n)
{
    // Your code goes here
    string s = "";
    f(n,s);
    sort(v.rbegin(),v.rend());
    return v;
}
};
