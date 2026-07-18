class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = []
        for i in range(9):
            column = [row[i] for row in board]

            columns.append(column)
        
        boxes = []
        
        for j in range(0, 9, 3):
            for i in range(0, 9, 3):
                box = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]
                boxes.append(box)
        
        all = board + columns + boxes

        for e in all:
            a = dict()
            
            for num in e:
                if num == ".":
                    continue
                
                a[num] = a.get(num, 0) + 1

                if a[num] > 1:
                    return False
            
        return True