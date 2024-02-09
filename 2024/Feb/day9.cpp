class Solution{
    public:
    int rec(Node *root)
    {
        if(root==0)
            return 0;
        if(root->left==0 && root->right==0)
            return root->data;
            
        int l=rec(root->left);
        int r=rec(root->right);
        
        if(l+r==root->data)
            return root->data;
        return -1000000;
    }
    
    int isSumProperty(Node *root)
    {
     // Add your code here
     int ans=rec(root);
        if(ans<0)
            return 0;
        return 1;
    }
};
