class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if nums[-1] < target : return len(nums)

        i = 0
        while target > nums[i] and i+1 < len(nums):
            i += 1
        else :
            return i
