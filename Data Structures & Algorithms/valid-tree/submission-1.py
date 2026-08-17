class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        parents = [ i for i in range(n)]
        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x
       
        def union(u,v):
            
            while parents[v] != v:
                v = parents[v]
            while parents[u] != u:
                u = parents[u]
            parents[u] = v
            return True

        for x,y in edges:    
            if find(x) == find(y):
                return False
            union(x,y)   
        return True 