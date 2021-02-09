# WIP - NOT FINISHED

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """        
        def fibonacci(n):
            if n <= 1:
                return n
        
            return fibonacci(n-1) + fibonacci(n-2)
        
        return fibonacci(n + 1)
        
      
