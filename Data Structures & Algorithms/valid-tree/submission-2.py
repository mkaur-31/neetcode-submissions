class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1: return False
        parents = [ i for i in range(n)]
        def find(x):
            while parents[x] != x:
                x = parents[x]
            return x
       
        def union(u,v):
            pu = find(u)
            pv = find(v)
            if pu == pv: return False
            
            
            
            parents[pu] = pv
            return True

        for x,y in edges:    
            if not union(x,y):
                return False
            
        return True 