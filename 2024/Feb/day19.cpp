class Solution{
public:
    int minValue(string s, int k){
        // code here
        unordered_map<char, int> maps;
        for (int i = 0; i < s.length(); i++){
            maps[s[i]]++;
        }


        for (int i = 0; i < k; i++){
            char c = '\0';
            int max = INT_MIN;
            for(const auto& pair: maps){
                if(pair.second > max){
                    max = pair.second;
                    c = pair.first;
                }
            }
            maps[c]--;
        }
        int res = 0;
        for (int i = 0; i < s.length(); i++){
            res += pow(maps[s[i]], 2);
            //cout << "maps[" << s[i] << "] =" << maps[s[i]] << endl;
            maps[s[i]] = 0;
        }
        return res;
    }
};
