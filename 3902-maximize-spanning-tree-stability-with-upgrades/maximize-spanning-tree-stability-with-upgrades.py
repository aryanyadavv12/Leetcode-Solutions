class Solution:
    #Aryan
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))
        size = [1] * n
        
        def find(v):
            if parent[v] == v:
                return v
            parent[v] = find(parent[v])
            return parent[v]
        
        def union(a, b):
            a = find(a)
            b = find(b)
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
                return True
            return False

        comp = n
        res = float("inf")
        opt = []
        for idx, edge in enumerate(edges):
            if edge[3] == 1:
                if union(edge[0], edge[1]):
                    comp -= 1
                    res = min(res, edge[2]) 
                else:
                    return -1  
        
        if comp == 1:  
            return res
        
        opt = [idx for idx, edge in enumerate(edges) if edge[3] == 0]

        opt.sort(key=lambda x: edges[x][2], reverse=True)
        
        stab = [] 
        
        for i in opt:
            edge = edges[i]
            if union(edge[0], edge[1]):
                comp -= 1
                stab.append(edge[2]) 
                if comp == 1:  
                    break
        
        if comp > 1: 
            return -1

        for i in range(1, min(len(stab), k) + 1):
            stab[-i] *= 2  
        return min(min(stab, default=res), res)