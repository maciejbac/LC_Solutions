class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        for i in range(len(nums)):
            if nums[i] == target: # Search for exact match, if found, return the index of the match
                return i
            
            if nums[i] > target: # If match not found, return the index of the next biggest number 
                return i         # Inserting the target at the index of next biggest number will
                                 # shift the entire remainder of the array to the right
        # If the target would be the largest number in the array, leave it at the end of the array
        return len(nums)   
