import math
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        output = []
        nbr = 0
        i=0
        #Convert the array in int, from [1,2,9] + 1 to [1,3,0] 
        for digit in digits:
            nbr = nbr*10 + digit 
        nbr += 1
        size_nbr = len(str(nbr))
        #Convert int to array
        while i<size_nbr:
            digit = str(nbr)[i]
            output.append(int(digit))
            i += 1
        return output
        