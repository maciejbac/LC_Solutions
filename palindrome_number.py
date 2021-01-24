class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if((x < 0) or (x % 10 == 0 and x != 0)):
            return False
        if(x == 0):
            return True
        
        reverted = 0
        
        while x > reverted:
            reverted = reverted * 10 + x % 10
            x = x / 10
            
            if len(str(x)) % 10 == 1:
                reverted = reverted/10

            if x == reverted or x == reverted/10:
                return True
            
