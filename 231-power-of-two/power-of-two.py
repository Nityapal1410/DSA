class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        #base case
        if n<=0:  #negative integers
            return False
        if n==1: #special case 
            return True
        if n%2 != 0 : #odd integers 
            return False
        #recursive case
        return self.isPowerOfTwo (n//2)
            

        
          
            