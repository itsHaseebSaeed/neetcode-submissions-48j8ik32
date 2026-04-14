class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #check if the target is at the start
        def is_before(i):
            num_cols = len(matrix[0])
            row,cols = i//num_cols,i % num_cols
            return matrix[row][cols] < target
        l,r = 0, len(matrix)*len(matrix[0]) - 1

        if matrix[0][l] >= target or matrix[len(matrix)-1][len(matrix[0])-1] < target:
            if matrix[0][l] == target:
                return True
            return False

        while r - l > 1:
            mid = (r+l)//2
            if is_before(mid):
                l = mid
            else:
                r = mid

        return matrix[r//len(matrix[0])][r%len(matrix[0])] == target
                


