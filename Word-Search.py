class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.m = len(board)
        self.n = len(board[0])
        self.word = word
        self.board = board
        
        self.dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        
        #edge case
        if len(self.word)>self.m*self.n:
            return False
        
        #logic
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j]==word[0]:
                    if self.dfs(i,j,0):
                        return True
        return False
    
    def dfs(self,i,j,index):
        #base case
        if index == len(self.word):
            return True
        
        if i<0 or i==self.m or j<0 or j==self.n or self.board[i][j]=="#":
            return False
        
        if self.board[i][j]==self.word[index]:
            #action
            self.board[i][j]="#"
            
            for x,y in self.dirs:
                nr = i + x
                nc = j + y
                
                #recurse
                if self.dfs(nr,nc,index+1):
                    return True
            #backtrack
            self.board[i][j] = self.word[index]
        return False