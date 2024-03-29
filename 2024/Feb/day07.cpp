class Solution{
    public:
    
    Node* lca(Node* root, int a, int b){
        if(root == NULL) return NULL;
        if(root->data == a || root->data == b) return root;
        Node* left = lca(root->left, a, b);
        Node* right = lca(root->right,a, b);
        if(right == NULL){
            return left;
        }
        else if(left == NULL){
            return right;
        }
        else{
            return root;
        }
    }
    
int solve(Node* root, int val){
    if(root == NULL)return 0;
    if(root->data == val)return 1;
    int a = solve(root->left, val);
    int b = solve(root->right, val);
    if(!a and !b)return 0;
    else return a+b+1;
}
    int findDist(Node* root, int a, int b) {
        Node* LCA = lca(root, a, b);
        int x = solve(LCA,a);
        int y = solve(LCA,b);
        return x+y-2;
    }
};
