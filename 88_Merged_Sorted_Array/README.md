# [PY] Merge 2 arrays into 1 sorted array
## Problem description 
You are given two integer arrays ```nums1``` and ```nums2```, sorted in non-decreasing order, and two integers ```m``` and ```n```, representing the number of elements in ```nums1``` and ```nums2``` respectively.
Merge ```nums1``` and ```nums2``` into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
>  Output: [1,2,2,3,5,6]

## Approach
*Selection sort algotihm  :*
1. Set MIN to location 0.
2. Search the minimum element in the list.
3. Swap with value at location MIN.
4. Increment MIN to point to next element.
5. Repeat until the list is sorted.

## Complexity
    O ( n^2 ) 


## Code
```python []
class Solution(object):
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






    

```
