# Solution derived from Kadane's algorithm. Explanation found here: 
# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        maxSoFar = -10000
        maxEndingHere = 0
        
        for i in range(len(nums)):
            maxEndingHere = maxEndingHere + nums[i]

            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
                
            if maxEndingHere < 0:
                maxEndingHere = 0
                
        return maxSoFar
            
