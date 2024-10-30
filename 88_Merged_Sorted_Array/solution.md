# [PY] Merge 2 arrays into 1 sorted array
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
