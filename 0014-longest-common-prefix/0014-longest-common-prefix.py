class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = strs[0] # Initialize prefix as the first string
        for i in range (1,len(strs)): 
            word = strs[i]
            while not word.startswith(prefix):  
                prefix = prefix[:-1]  # Reduce prefix by removing the last character
        return prefix


