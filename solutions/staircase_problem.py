# WIP - NOT FINISHED, TOO SLOW FOR LEETCODE AND TIMES OUT

# Resources:
"""
Remember the formula: ways(n) = ways(n-1) + ways(n-2)
ways(4) = ways(3) + ways(2)
ways(3) = ways(2) + ways(1)
ways(2) = ways(1) + ways(0)
ways(1) = 1
ways(0) = 1
This is the iterative Fibonacci Solution!

https://quanticdev.com/algorithms/dynamic-programming/staircase-problems/
"""

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """        
        
        if n <= 3: # Below n = 3, fibonnaci sequence returns the same value as the n so no calculations required
            return n
        
        # the number of combinations for n is the same as (n-1) + (n-2)
        # Recursively calculate the number of combinations for n-1 and n-2 
        total = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return total

    
    
    # Seems like recursive approach isn't working out here, need to refactor it and try sequential 
