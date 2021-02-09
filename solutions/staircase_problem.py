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
        
        if n <= 3:
            return n
        
        total = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        
        return total
