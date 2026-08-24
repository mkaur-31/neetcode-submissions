class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        DIR = ((-1,0), (1,0), (0,1), (0,-1))
        self.res = 0
       
        
    
        def dfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = 2
            print(r,c)
            while queue:
                r,c  = queue.popleft()
                self.res += int(r == 0) + int(c == 0) + int(r == ROWS-1) + int(c == COLS -1)              
                for i,j in DIR:
                    _r, _c = r+i, c+j
                    if _r >=0 and _c >= 0 and _r <= ROWS-1 and _c <= COLS-1:
                        if grid[_r][_c] == 1:
                            grid[_r][_c] = 2
                            queue.append((_r,_c))
                        elif grid[_r][_c] == 0:
                            self.res += 1
        found = False
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j]:
                    dfs(i,j)
                    found = True
                    break
            if found:
                break
        return self.res

        