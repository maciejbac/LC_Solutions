class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        result = 0
        
        # Detect if the integer is negative. If yes, convert it to positive and store the information for later.
        if x < 0:
            x = x * -1
            negative = True
            
        
        # Pop the least significant digit of the x and truncate x accordingly
        for i in range(len(str(x))): 
            pop = x % 10
            x = x/10
            
            # Concatanate already obtained result with the most recently popped number
            result = int(str(result)+str(pop))
        
        # Detect if the resulting number is exceeding 32bits, return 0 if yes
        if((result < (-2**31)) or (result > (2**31))):
            return 0 
           
        # Turn the result negative if the original value was also negative
        if negative:
            result = result * -1
            
        return result
