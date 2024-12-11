def strToBin(val:str) -> int:
    digit_val = []
    bin_val = 0
    i=0
    while i<len(val):
        #Convert the list to binary using a right shift.
        digit_val.append(int(val[i]))
        bin_val = (bin_val << 1) + digit_val[i]  
        i+=1
    return bin_val

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = strToBin(a)+strToBin(b)
        output = str(bin(res))
        return output[2:]

