class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [[False for i in range(n)] for j in range(n)]
        self.result = []
        self.backtrack(board,0)
        return self.result
    
    def backtrack(self,board,r):
        #base case
        if r==len(board):
            #build output string
            row = []
            for i in range(len(board)):
                stringBuilder = ""
                for j in range(len(board)):
                    if board[i][j]:
                        stringBuilder += "Q"
                    else:
                        stringBuilder += "."
                row.append(stringBuilder)
            self.result.append(row)
            return
        
        #logic
        for c in range(len(board)):
            if self.isSafe(board,r,c):
                board[r][c] = True
                
                self.backtrack(board,r+1)
            board[r][c] = False
            
    def isSafe(self,board,i,j):
        #column check
        for r in range(0,i):
            if board[r][j]:
                return False
        
        r=i
        c=j
        #left diagonal check
        while r>=0 and c>=0:
            if board[r][c]:
                return False
            r-=1
            c-=1
        r=i
        c=j
        #right diagonal check
        while r>=0 and c<len(board):
            if board[r][c]:
                return False
            r-=1
            c+=1
            
        return True