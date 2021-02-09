# Solution derived from Kadane's algorithm. Explanation found here: 
# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        maxFound = -100000
        maxHere = 0
        
        for i in range(len(nums)):
            maxHere = maxHere + nums[i]

            if maxFound < maxHere:
                maxFound = maxHere
                
            if maxHere < 0:
                maxHere = 0
                
        return maxFound
            
            
