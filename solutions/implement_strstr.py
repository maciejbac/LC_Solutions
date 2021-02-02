class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if needle == '': # Return 0 if needle is empty
            return 0
        
        if needle in haystack: # If needle is found in the string, use the index() function to determine the index of the first letter
            return haystack.index(needle)
        
        # Return -1 if the needle is not found
        return -1 
