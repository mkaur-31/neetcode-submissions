class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        nodes = set([i+1 for i in range(n)])

        adj = defaultdict(list)
        for x,y,t in times:
            adj[x].append((y,t))

        queue = deque([(k,0)])
        res = [float('inf')]*(n)
        res[k-1] = 0
        
        

        while queue:
            u,t = queue.popleft()
    
            for v, tnode in adj[u]:
                new_t = t + tnode
                if res[v-1] > new_t:
                    res[v-1] = new_t
                    queue.append((v, new_t))

        del_t = max(res)
        return -1 if del_t == float('inf') else del_t
            