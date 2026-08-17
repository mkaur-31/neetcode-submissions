class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
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
        res = n

        for x,y in edges:    
            if union(x,y):
                res -= 1

            
        return res 
        