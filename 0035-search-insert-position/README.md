## [35. Search Insert Position](https://leetcode.com/problems/search-insert-position)

**Difficulty**: Easy

### Problem Statement
Given a sorted array of distinct integers `nums` and a target value `target`, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with `O(log n)` runtime complexity.

### Examples
**Example 1:**
Input: nums = [1,3,5,6], target = 5 Output: 2

**Example 2:**
Input: nums = [1,3,5,6], target = 2 Output: 1


**Example 3:**
Input: nums = [1,3,5,6], target = 7 Output: 4


# Approach
Finds the insertion index of a target in a sorted list, returning the index where it should be placed if not found.
Comparing the target in ascending order to each value in the list.

1. **Edge Case Check**: If the last element in `nums` is smaller than `target`, it returns the length of `nums`, as `target` would be placed at the end.
2. **Iterative Search**: Initializes `i` at `0` and iterates through `nums` while `target` is greater than `nums[i]` and `i` remains within bounds.
3. **Result Return**: The loop terminates when the right insertion point is found, and `i` is returned as the index for insertion.

## Time Complexity
	O(n)

# Code
```python3 []
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if nums[-1] < target : return len(nums)

        i = 0
        while target > nums[i] and i+1 < len(nums):
            i += 1
        else :
            return i

```

