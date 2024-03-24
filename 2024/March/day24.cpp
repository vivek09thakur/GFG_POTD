class Solution{
public:
    stack<int> insertAtBottom(stack<int> s,int x){
        stack<int> q;
        while(!s.empty()){
             q.push(s.top());
             s.pop();
        }
        s.push(x);
        while(!q.empty()){
             s.push(q.top());
             q.pop();
        }
        return s;
    }
};
