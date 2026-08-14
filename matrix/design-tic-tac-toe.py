class TicTacToe:

    def __init__(self, n: int):
       self.n=n
       self.rows=[0]*n
       self.cols=[0]*n
       self.diag=0
       self.anti=0

    def move(self, row: int, col: int, player: int) -> int:
        n=self.n
        k=1 if player==1 else -1
        
        self.rows[row]+=k #row
        self.cols[col]+=k #cols
        if row==col:
            self.diag+=k #diag
        if row+col==n-1:
            self.anti+=k #antidiag
            
        if abs(self.rows[row])==n or abs(self.cols[col])==n or abs(self.diag)==n or abs(self.anti)==n:
            return player
        
        return 0
            
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)