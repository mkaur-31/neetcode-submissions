class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       

        adj = defaultdict(list)
        for x,y,t in times:
            adj[x].append((y,t))

        minHeap = [(0,k)]
        visit = set()
        res = 0

        while minHeap:
            t, u = heapq.heappop(minHeap)
            if u in visit:
                continue
            visit.add(u)
            res = t
            
    
            for v, tnode in adj[u]:
                if v not in visit:
                   heapq.heappush(minHeap, (tnode+t, v))

        
        return res if len(visit)==n else -1
            