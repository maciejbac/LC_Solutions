class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        accumulator = 0
        last = 1000
        
        for i in range(len(s)):
            num = roman[s[i]]
            print(num)
            
            if last < num:
                accumulator = accumulator - last - last + num
                last = num
            else:
                accumulator = accumulator + num
                last = num

        return accumulator
