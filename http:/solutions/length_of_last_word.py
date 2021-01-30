class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Split the string s into an array of words
        wordList = s.split()
        for i in range(len(wordList)): # Iterate through all words in the array
            wordList[i] = wordList[i].strip() # Remove whitespace from the words to prevent it from being counted and to catch empty s inputs
        
        
        if wordList: # If s input was empty, this statement will be false and program will return 0
            return len(wordList[len(wordList)-1]) # If the wordList variable contains 1=< characters, return the length of the last (length-1) word
        else:
            return 0 # Return 0 if wordList is empty
