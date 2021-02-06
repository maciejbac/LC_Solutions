class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        result = x ** 0.5 # Calculate the x to the power of 0.5
        return int(result) # Cast the result as int to truncate decimal places and return it

    
    
# todo: re-invent the wheel by coding this using the babylonian square root method instead
