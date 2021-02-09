class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        maxSoFar = -10000
        maxEndingHere = 0
        
        if len(nums) == 1:
            return nums[0]
        
        for i in range(len(nums)):
            maxEndingHere = maxEndingHere + nums[i]

            if maxSoFar < maxEndingHere:
                maxSoFar = maxEndingHere
                
            if maxEndingHere < 0:
                maxEndingHere = 0
                
        return maxSoFar
            
