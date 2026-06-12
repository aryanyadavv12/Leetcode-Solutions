class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        MOD = 10**9 + 7
        LOG = 17

        adj = [[] for _ in range(n + 1)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = [0] * (n + 1)
        up = [[0] * (n + 1) for _ in range(LOG)]
        seen = [False] * (n + 1)
        queue = deque([1])
        seen[1] = True

        while queue:
            u = queue.popleft()
            for v in adj[u]:
                if not seen[v]:
                    seen[v] = True
                    depth[v] = depth[u] + 1
                    up[0][v] = u
                    queue.append(v)

        for j in range(1, LOG):
            for i in range(1, n + 1):
                up[j][i] = up[j-1][up[j-1][i]]

        def lca(u, v):
            if depth[u] < depth[v]:
                u, v = v, u
            diff = depth[u] - depth[v]
            for j in range(LOG):
                if (diff >> j) & 1:
                    u = up[j][u]
            if u == v:
                return u
            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u, v = up[j][u], up[j][v]
            return up[0][u]

        pw = [1] * (n + 1)
        for i in range(1, n + 1):
            pw[i] = pw[i-1] * 2 % MOD

        result = []
        for u, v in queries:
            d = depth[u] + depth[v] - 2 * depth[lca(u, v)]
            result.append(0 if d == 0 else pw[d - 1])
        return result