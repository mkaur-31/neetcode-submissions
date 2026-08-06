class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])
        i = 0
        j = (r * c )-1
        
        while i <= j:

            mid = i+ (j-i)//2
            tr = mid // c
            tc = mid % c
            if matrix[tr][tc]==target:
                return True
            elif matrix[tr][tc] < target:
                i = mid+1
            else:
                j = mid - 1
        return False

        