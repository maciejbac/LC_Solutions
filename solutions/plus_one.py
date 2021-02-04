class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        total = 0 # Initial total variable
        init = len(digits) # Save the length of the original array for further use
        
        for i in range(len(digits)): # Iterate through the initial array and convert it to an integer
            multiplier = 10 ** (len(digits) -1 - i) # Generate multiplier for each iteration of the loop, so that if i=0 we work on units, i=1 10's etc.
            total = digits[i] * multiplier + total  # Add the (digit * multiplier) to the current total
        
        total += 1 # Increment total by 1 as per requirement 
        total = map(int, str(total)) # generate a new array based on the total
        
         # While loop to pad out the array with zeros, in case the inital array comes with 0 at the beginning that will be lost
            # during the integer assembly loop
        while len(total) < init:
            total.insert(0, 0) 
         
        return total
    
    
    # Todo
    # Remove unneccesary variables such as multiplier
