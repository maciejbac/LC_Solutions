class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        total = 0
        init = len(digits)
        
        for i in range(len(digits)):
            multiplier = 10 ** (len(digits) -1 - i)          
            total = digits[i] * multiplier + total
        
        total += 1
        total = map(int, str(total))
        
        while len(total) < init:
            total.insert(0, 0)
        
        return total
        
        
        
        # Todo comment
