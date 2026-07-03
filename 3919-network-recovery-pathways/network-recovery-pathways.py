class Solution:
    def evaluate(self, adj: List[List[tuple(int, int)]], topo: List[int], k: int, threshold: int) -> bool:
        n = len(topo)
        dist = [k + 1] * n
        dist[0] = 0
        for u in topo:
            for v, cost in adj[u]:
                if cost < threshold:
                    continue
                dist[v] = min(dist[v], dist[u] + cost)
        return dist[-1] <= k


    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        ind = [0] * n
        max_cost = -1
        adj = [[] for _ in range(n)]
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                ind[v] += 1
                max_cost = max(max_cost, cost)

        topo = []
        q = deque()
        for u in range(n):
            if ind[u] == 0:
                q.append(u)
        
        while q:
            u = q.popleft()
            topo.append(u)
            for v, cost in adj[u]:
                ind[v] -= 1
                if ind[v] == 0:
                    q.append(v)

        l = -1
        r = max_cost + 1
        while l < r - 1:
            mid = l + (r - l) // 2
            if self.evaluate(adj, topo, k, mid):
                l = mid
            else:
                r = mid
        return l