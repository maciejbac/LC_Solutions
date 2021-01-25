class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        # Iterate through all combinations of numbes with a double for loop that essentially
        # generates a grid of sums based on values from the list, for example:
        # List1 = [1, 3, 5]
        # 
        
        #    1  3  5
        # 1  x  4  6
        # 3  4  x  8
        # 5  6  8  x
        #
        
        for i in range(len(nums)):
            for j in range(len(nums)): # Avoid using the same indexes in iterators to prevent using the same value twice
                if i == j: 
                    break
                test = nums[i] + nums[j] 
                if test == target: # Iterate through all result sums and return the values that add up to the target value
                    return [i, j]
