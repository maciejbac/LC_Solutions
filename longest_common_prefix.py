class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if len(strs) == 0:
            return ''
        
        shortest = strs[0]
        found = 0
        
        for i in range(len(strs)):
            if len(strs[i]) < len(shortest):
                shortest = strs[i]

        while shortest:
            for i in range(len(strs)):
                findVal = strs[i].find(shortest, 0, len(shortest))
                if findVal != -1:
                    found = found + 1

            if found >= len(strs):
                return shortest
            else:
                found = 0
                shortest = shortest[:-1]

        
        return ''
