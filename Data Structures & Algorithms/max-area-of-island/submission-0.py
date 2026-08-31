class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid,r,c):
            nonlocal area
            for i, j  in DIR:
                _r , _c = r+i, c+j
                if _r >=0 and _c >=0 and _r < ROWS and _c < COLS and grid[_r][_c]==1:
                    grid[_r][_c] = 0
                    area += 1
                    dfs(grid,_r,_c)
            return
        


        if not grid[0]:
            return 0

        res = area = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        DIR = [(-1,0),(0,-1),(1,0),(0,1)]
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    grid[i][j] = 0
                    area += 1
                    dfs(grid, i, j)
                    res = max(area,res)
                    area = 0
        return res

        