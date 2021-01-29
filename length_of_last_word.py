class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordList = s.split()
        for i in range(len(wordList)):
            wordList[i] = wordList[i].strip()
        
        
        if wordList:
            return len(wordList[len(wordList)-1])
        else:
            return 0
            
            
            # todo ## comment the code 
