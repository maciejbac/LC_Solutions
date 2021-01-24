class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Determine if the number is negative or if it's divisible by 10 to exclude numbers that cannot be palindromes, i.e. -1, 10, 120 etc.
        if((x < 0) or (x % 10 == 0 and x != 0)):
            return False
        if(x == 0):
            return True # Zero will always be a 1 digit palindrome
        
        reverted = 0
        
        while x > reverted:
            reverted = reverted * 10 + x % 10 # Shift current reverted number by 1 digit to the left, then add mod10 remainder of the x
            x = x / 10 # Divide x by 10 to truncate it before next pass of the loop
            
            if len(str(x)) % 10 == 1: # Detect if we're working with an odd-length palindrome, if yes, truncate it by 1 most significant digit
                reverted = reverted/10

            if x == reverted or x == reverted/10: # Return True if the reverted half of the integer is the same as it's mirror reflection
                return True
            
