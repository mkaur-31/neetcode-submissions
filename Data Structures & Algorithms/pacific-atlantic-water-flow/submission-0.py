class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]: return []

        ROWS = len(heights) 
        COLS = len(heights[0])
        DIR = ((-1,0),(1,0),(0,-1),(0,1))

        pacific_reach = set()
        atlantic_reach = set()

        def dfs(r,c , reach):
            reach.add((r,c))
            for x,y in DIR:
                _r = r + x
                _c = c + y
                if _r < 0 or _r >= ROWS or _c < 0 or _c >= COLS or (_r,_c) in reach or heights[_r][_c] < heights[r][c]:
                    continue
                dfs(_r,_c,reach)


        
        for i in range(ROWS):
            dfs(i,0, pacific_reach)
            dfs(i, COLS-1,atlantic_reach)
        for i in range(COLS):
            dfs(0,i,pacific_reach)
            dfs(ROWS-1,i,atlantic_reach)
        return list( pacific_reach.intersection(atlantic_reach))
        
        
        