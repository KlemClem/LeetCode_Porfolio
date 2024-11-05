## [13. Roman to Integer](https://leetcode.com/problems/roman-to-integer)
**Difficulty**: Easy

### Problem Statement
Roman numerals are represented by seven different symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

For example:
- `2` is written as `II`, which is two ones added together.
- `12` is written as `XII`, which is `X + II`.
- `27` is written as `XXVII`, which is `XX + V + II`.

Roman numerals are typically written from largest to smallest left to right. However, certain numerals use subtraction (e.g., `IV` for 4 and `IX` for 9). The following rules apply for subtraction:
- `I` can be placed before `V` (5) and `X` (10) to make 4 and 9.
- `X` can be placed before `L` (50) and `C` (100) to make 40 and 90.
- `C` can be placed before `D` (500) and `M` (1000) to make 400 and 900.

Given a Roman numeral, convert it to an integer.

### Examples
**Example 1:**
Input: s = "III", Output: 3, Explanation: III = 3

**Example 2:**
Input: s = "LVIII", Output: 58, Explanation: L = 50, V = 5, III = 3

**Example 3:**
Input: s = "MCMXCIV", Output: 1994, Explanation: M = 1000, CM = 900, XC = 90, IV = 4
# Approach
This function converts a Roman numeral string to an integer by iterating through the string, adding values from a dictionary for single and two-character (special case) numerals.

1. Conversion Dictionaries
```conversion_dict``` maps each Roman numeral character to its integer value.
```special_case_dict``` stores special two-character combinations that follow the subtraction rule, like "IV" for 4 and "IX" for 9.

2. While Loop to Traverse the String
```while i < size:```
We initialize i to 0, which represents the current index in the string.
The loop will continue until i reaches the length of the string, size.

3. Checking & Processing for Special Cases
```if i < size - 1 and s[i:i+2] in special_case_dict:```
This condition checks whether:
    - There are at least two characters remaining (i < size - 1), and
    - The next two characters (s[i:i+2]) match a special case in special_case_dict.
    
    ```If``` **a special case is found**, we add its value to total (e.g., 900 for "CM").
    i is then incremented by 2 to skip the next character since the special case spans two characters.

4. Processing Regular Cases (Else)
 ```total += conversion_dict[s[i]]```
If no special case is found, the single character s[i] is processed by adding its value from conversion_dict to total.
i is then incremented by 1 to move to the next character.


##### Example
For the input "MCMXCIV":

```"M"```: Not a special case, so total becomes 1000.
```"CM"```: Special case; we add 900, making total 1900, and skip to the next character after "M".
```"XC"```: Special case; we add 90, making total 1990, and skip to the next character after "C".
```"IV"```: Special case; we add 4, making total 1994.
Thus, the function correctly returns 1994 for this input.
# Complexity
O(n)

# Code
```python []
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

```
