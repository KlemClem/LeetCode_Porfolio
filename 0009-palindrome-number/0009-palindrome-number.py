class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
  
       # Early return for negative numbers
        if x < 0:
            return False

        x_string = str(x)
        k = len(x_string) - 1

        # Loop through the string up to the midpoint
        for i in range(len(x_string) // 2):
            if x_string[i] != x_string[k - i]:
                return False  # If any characters don't match, it's not a palindrome
        
        return True  # All characters matched, so it's a palindrome