class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        res = area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        DIR = [(-1,0),(0,-1),(1,0),(0,1)]

        if not grid[0] : return 0
        res = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    stack = deque([(i,j)])
                    grid[i][j] = 0
                    area = 0

                    while stack: 
                        r , c = stack.popleft()                   
                        area += 1
                        for x,y in DIR:
                            nr = r + x
                            nc = c + y
                            if nr >= 0 and nc >= 0 and nr < ROWS and nc < COLS and grid[nr][nc]:
                                grid[nr][nc] = 0
                                stack.append((nr,nc))
                    res = max(area,res)
        return res
            