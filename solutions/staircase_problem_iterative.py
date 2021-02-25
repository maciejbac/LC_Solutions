class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """        
        
        a, b = 1, 1
            
        for node in range(n-1):
            next_b = a + b
            a = b
            b = next_b
                
        return b
        
