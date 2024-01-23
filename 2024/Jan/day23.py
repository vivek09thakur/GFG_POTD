class Solution:
    def findOrder(self, n, m, prerequisites):
        # Code here
        from collections import defaultdict
        g = defaultdict(list)
        degree = [0]*n
        for to, frm in prerequisites:
            g[frm].append(to)
            degree[to] += 1
        
        q = [i for i, e in enumerate(degree) if e == 0]

        orders = []
        while q:
            node = q.pop()
            orders.append(node)
            for nbr in g[node]:
                degree[nbr] -= 1
                if degree[nbr] == 0:
                    q.append(nbr)
        return orders if len(orders) == n else []
