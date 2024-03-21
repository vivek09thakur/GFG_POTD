class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        queue = [[root]]
        res = []
        check = False
        while len(queue) != 0:
            temp = queue.pop()
            nodes = []
            val = []
            for one in temp:
                val.append(one.data)
                if one.left:
                    nodes.append(one.left)
                if one.right:
                    nodes.append(one.right)
            if len(nodes) > 0:
                queue.append(nodes)
            if check:
                res.extend(val[::-1])
                check = False
                continue
            check = True
            res.extend(val)
            
        return res
