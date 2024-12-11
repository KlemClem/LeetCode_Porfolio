class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:    
            idx = nums.index(val)  #Return idx of the value to pop
            nums.pop(idx)   
        