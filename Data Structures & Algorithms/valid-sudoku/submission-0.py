class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        i , j , x, y = 0,0 ,9,9
        col_set = [set() for i in range(x)]
        sq_set = [set() for i in range(x)]
        def in_sq (i,j,val):
            sq =( i//3 * 3 ) + j//3
            if val in sq_set[sq]:
                return True
            sq_set[sq].add(val)
            return False

     
        while i < x:
            row_set = set()
            
            while j < y:
                val = board[i][j]
                if val != '.' :
                    if val in row_set or val in col_set[j]:
                        return False
                    row_set.add(val)
                    col_set[j].add(val)
                    if in_sq(i,j,val):
                        return False
                j+=1
            j = 0
            i += 1
        return True