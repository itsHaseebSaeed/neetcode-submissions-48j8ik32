class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [set() for _ in range(9)]
        rows = [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)]for _ in range(3)]

        for i,row in enumerate(board):
            for j,digit in enumerate(row):
                if digit == ".":
                    continue
                if digit in rows[i] or digit in cols[j] or digit in  boxes[i//3][j//3]:
                    return False
                rows[i].add(digit)
                cols[j].add(digit)
                boxes[i//3][j//3].add(digit)
            
        return True

