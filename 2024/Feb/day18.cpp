class Solution
{
    public:
        /*You are required to complete below method */
        void add(Node* root, int& sum){
            if (!root) return;
            if (root->left || root->right){
                if(root->left)add(root->left, sum);
                if(root->right)add(root->right, sum);
            }
            else sum += root->data;
        }
        int sumOfLeafNodes(Node *root ){
             int sum = 0;
             add(root, sum);
             return sum;
        }
};
