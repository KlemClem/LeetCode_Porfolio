class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conversion_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        special_case_dict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        size = len(s)
        total = 0
        i = 0
        while i < size:
            # Start by looking for a special case
            if i+1 < size and s[i:i+2] in special_case_dict :
                total = total + special_case_dict.get(s[i:i+2])  
                i += 2  # Condition handle 2-character-case, skip the next one
            else :
                total +=  conversion_dict.get(s[i])
                i+=1 # Move to next character
        return total
