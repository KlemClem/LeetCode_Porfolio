class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Creating hash map 
        dict_num_idx = {}

        # Going through array 
        for  idx, nbr in enumerate(nums):    
            difference = target - nbr

            if difference in dict_num_idx :
                return [idx, dict_num_idx[difference]]

            dict_num_idx[nbr] = idx

