class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = 0 # Set iterator variable to 0 
        
        # Continue until reached length of the array -1, I need the 1 index margin because I'm comparing numbers
        # with the index 1 step ahead, this prevents going past the last index
        while current < len(nums)-1: 
            if nums[current] == nums[current+1]: # If the current number is the same as the next number, pop it 
                nums.pop(current)
            else: # If no match was found, jump to the next index in the array
                current += 1 
