class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        negative = False
        result = 0
        
        if x < 0:
            x = x * -1
            negative = True
            
        
        for i in range(len(str(x))):
            pop = x % 10
            x = x/10
        
            result = int(str(result)+str(pop))
                    
        if((result < (-2**31)) or (result > (2**31))):
            return 0 
           
           
        if negative:
            result = result * -1
            
        return result
