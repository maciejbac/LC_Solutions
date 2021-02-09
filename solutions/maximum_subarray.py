# Solution derived from Kadane's algorithm. Explanation found here: 
# https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        
        # Define initial variables 
        maxFound = -100000 # maxFound set to the lowest number specified in the requirements
        maxHere = 0 # Local max to store maximum sum subarray length 
        
        for i in range(len(nums)): # Iterate through all the numbers in the array
            maxHere = maxHere + nums[i] # Add the nums[i] number to the existing highest sum 

            if maxFound < maxHere: # Compare highest found sum to the current sum to determine if the current maxHere is higher
                maxFound = maxHere
                
            # If maxHere is negative, set it to 0 to indicate that the highest sum array would be 0 (no numbers in array)
            if maxHere < 0:
                maxHere = 0
        
        # Return the highest sum subarray length
        return maxFound
            
            
