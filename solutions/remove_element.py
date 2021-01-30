class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums: # Remove elements of value val as long as they exist in the List nums
            nums.remove(val)
