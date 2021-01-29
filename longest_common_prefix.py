class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # Check if the input array is empty, return null if it is
        if len(strs) == 0:
            return ''
        
        # Initialise variables to ensure correct var type
        shortest = strs[0]
        found = 0
        
        # Find the shortest word in input array to reduce the amount of unneccesary operations
        for i in range(len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]

        # Continue as long as shortest > 0
        while shortest:
            for i in range(len(strs)): # Iterate through every string in the array 
                findVal = strs[i].find(shortest, 0, len(shortest)) # Search for the 'shortest' word at the beginning of the word
                if findVal != -1: # -1 is the return value of find() when nothing is found. 
                    found = found + 1 # Increase the found counter if the word is foundd

            if found >= len(strs): # Return the shortest word if it was found in every word in the array
                return shortest
            else: # If the word is not found, remove the last letter and try again with the truncated string
                found = 0
                shortest = shortest[:-1]

        # Return null if there's no common prefix and the shortest word has been truncated to 0        
        return ''
