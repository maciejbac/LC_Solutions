class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """      
        # Define pairs of valid parentheses
        par = ['()', '[]', '{}']
        
        # Continue as long as s isn't empty
        while s:          
            last = s # Save last value of s for comparison later
            
            for node in par: # Search for pairs of parentheses, replace them with nothing if found
                    s = s.replace(str(node), '')
                    
            # Compare last value of s and current value to determine if changes were made in the string.replace() function call
            # If no changes were made and s still contains characters, it means that no valid combination was found
            if last == s:
                return False
        
        # If the parentheses is valid, the while loop will run until s is empty, then return True
        return True
