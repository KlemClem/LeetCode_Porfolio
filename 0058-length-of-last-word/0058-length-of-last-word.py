class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = len(s)-1
        len_last_word = 0
        # Combine skipping spaces and counting the last word length
        while i >= 0:
            if s[i] == ' ':  
                # Verify that we are still cleaning the string 
                if len_last_word > 0:  
                    break  
            elif s[i].isalpha():
                len_last_word += 1
            
            i -= 1  # Always decrement i

        return len_last_word