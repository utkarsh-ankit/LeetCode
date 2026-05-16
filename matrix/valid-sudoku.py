class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):               #row
            k=set()
            for j in range(9):
                if board[i][j]==".":
                    continue
                elif board[i][j] in k:
                    return False
                k.add(board[i][j])
        for i in range(9):               #column (v imp)
            k=set()
            for j in range(9):
                if board[j][i]==".":     #the reverse of j and i
                    continue
                elif board[j][i] in k:
                    return False
                k.add(board[j][i])

        for br in (0,3,6):
            for bc in (0,3,6):
                k = set()
                for i in range(br, br+3):
                    for j in range(bc, bc+3):
                        v = board[i][j]
                        if v == ".":
                            continue
                        if v in k:
                            return False
                        k.add(v)
        return True



        