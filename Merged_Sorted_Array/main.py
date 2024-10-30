def merge(self, nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    l = m + n
    nums1[m:] = nums2
    print(nums1)

    for i in range(l-1):
        idx_min  = i
        for j in range(i+1,l):
            if (nums1[j] < nums1[idx_min] ):
                idx_min = j
        nums1[idx_min], nums1[i] = nums1[i], nums1[idx_min]



if __name__ == "__main__":
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1, m, nums2, n) 
 
