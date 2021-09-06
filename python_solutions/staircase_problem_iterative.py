# Recursive method can be found here: https://github.com/macko939/LC_Solutions/blob/main/solutions/staircase_problem.py

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """        
        
        a, b = 1, 1 # Initialise first two steps in the fibonacci sequence
            
        for node in range(n-1): # Use the range() function to determine how many steps of the fibonnacci sequence we need to calculate. 1 is taken away to avoid off-by-one errors.
            nextB = a + b       # Calculate the value of the next step of the fibbonaci sequence.
            
            a = b               # Rearrange variables to allow the calculation of the next step in the fibonacci sequence               
            b = nextB           
                
        return b
        
