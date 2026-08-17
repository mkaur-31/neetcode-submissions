class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import defaultdict
        indegree = defaultdict(int)
        adj = defaultdict(list)
        for dest, src in prerequisites:
             indegree[dest] += 1
             adj[src].append(dest)
        
        z_queue = deque([crs for crs in range(numCourses) if crs not in indegree])
        finish = 0
        while z_queue:
            cur = z_queue.popleft()
            finish+=1

            for ngh in adj[cur]:
                indegree[ngh] -= 1
                if indegree[ngh] == 0:
                    z_queue.append(ngh)

        return True if finish == numCourses else False

        
        
        
