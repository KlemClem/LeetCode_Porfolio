class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_pairs = {')': '(', ']': '[', '}': '{'}

        for char in s :
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif char == ')' or char == ']' or char == '}':
                if  stack and  stack[-1] == dict_pairs[char] :
                    stack.pop()
                else :
                    return False
        return not stack