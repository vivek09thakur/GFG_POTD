class Solution{
    public:
    int DivisibleByEight(string s){
        //code here
        return stoi(s.substr(s.size() - min(3, (int)s.size()))) % 8 == 0 ? 1 : -1;
    }
};
