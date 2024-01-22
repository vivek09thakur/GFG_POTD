class Solution:
    def printPaths(self, root, S):
        ans = 0
        nodes_list = []
    
        def dfs(node, path):
            nonlocal ans
            nonlocal nodes_list
        
            ans += node.data
            path.append(node.data)
        
            if ans == S:
                nodes_list.append(path[:])
        
            if node.left:
                dfs(node.left, path)
        
            if node.right:
                dfs(node.right, path)
        
            ans -= node.data
            path.pop()
    
        dfs(root, [])
        return nodes_list
