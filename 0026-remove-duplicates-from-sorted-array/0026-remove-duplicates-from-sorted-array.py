class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i in range(0,len(nums)):
            while i+1<len(nums) and nums[i+1]==nums[i]:
                nums.pop(i+1)
                k += 1
        print(k, 'nums =',nums)
