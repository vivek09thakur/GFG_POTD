class Solution{
public:
	// The main function that returns the arrangement with the largest value as
	// string.
	// The function accepts a vector of strings
    struct Compare {
        bool operator()(const string& a, const string& b) const {
            return (a + b) < (b + a);
        }
    };
	string printLargest(int n, vector<string> &arr) {
	    // code here
	    priority_queue<string, vector<string>, Compare> pq;
        string str = "";

        for(auto it : arr){
            pq.push(it);
        }

        while(!pq.empty()){
            str += pq.top();
            pq.pop();
        }

        return str;
	}
};
