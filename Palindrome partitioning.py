class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        self.result = []
        self.backtrack(s,0,[])
        return self.result
    
    def backtrack(self,s,pivot,path):
        #base case
        if pivot == len(s):
            self.result.append(path[:])
        
        #logic
        for i in range(pivot,len(s)):
            subString = s[pivot:i+1]
            if self.isPalindrome(subString):
                #action
                path.append(subString)
                
                #recurse
                self.backtrack(s,i+1,path)
                
                #backtrack
                path.pop()
                
    def isPalindrome(self,subString):
        left = 0
        right = len(subString)-1
        while left<right:
            if subString[left]!=subString[right]:
                return False
            left+=1
            right-=1
        return True