class Solution
{
private:
    void traverseTree(vector<int> &v, Node *node)
    {
        if(node->left)
        {
            traverseTree(v, node->left);
        }
        v.push_back(node->data);
        if(node->right)
        {
            traverseTree(v, node->right);
        }
    }
public:
    Node *flattenBST(Node *root)
    {
        // code here
        vector<int> v;
        traverseTree(v, root);
        Node *ansHead = new Node(v[0]);
        Node *curr = ansHead;
        for(int i=1; i<v.size(); i++)
        {
            curr->right = new Node(v[i]);
            curr = curr->right;
        }
        return ansHead;
    }
};
