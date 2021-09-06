class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        sum = bin(int(a,2) + int(b,2)) # Convert a and be to binary using int(x,2) where 2 is the base of the system desired
        return sum[2:] # Truncate first 2 characters of sum that encode the base system (0b) and return it
