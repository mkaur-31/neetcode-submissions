from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i , j , x, y = 0,0 ,9,9
        cols = defaultdict(set)
        squares = defaultdict(set)

     
        for r in range(9):
            row = set()            
            for c in range(9):
                val = board[r][c]
                if val != '.' :
                    if (val in row
                        or val in cols[c]
                        or val in squares[(r//3,c//3)]):
                        return False
                    row.add(val)
                    cols[c].add(val)
                    squares[(r//3,c//3)].add(val)                
        return True