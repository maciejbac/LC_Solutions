class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create a dictionary of roman numerals for easy conversion
        roman = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

        accumulator = 0
        last = 1000
        
        # Iterate through all characters in the roman sequence
        for i in range(len(s)):
            num = roman[s[i]] 
            print(num)
            
            # Detect subtractive roman numerals by comparing previous number with the current one.
            # If the previous number is smaller than the current number, reverse the last addition and substract
            # the last number from the current number instead. If no subtractive numeral is detected, proceed with
            # simply adding numeral values to the accumulator.
            if last < num:
                accumulator = accumulator - last - last + num
                last = num
            else:
                accumulator = accumulator + num
                last = num

        return accumulator
