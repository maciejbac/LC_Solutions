class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """      
        par = ['()', '[]', '{}']
        
        while s:          
            last = s
            
            for node in par:
                    s = s.replace(str(node), '')
                    
            if last == s:
                return False
                    
        return True
