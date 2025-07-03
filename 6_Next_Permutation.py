Leatcode Result:- https://leetcode.com/problems/next-permutation/submissions/1685082268

"""Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]"""

"""Please go thourgh step by step for better understanding"""

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
      
        n = len(nums)
        i = n - 2
        
        # Step 1: Find first decreasing element from the right
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        if i >= 0:
            # Step 2: Find element just larger than nums[i]
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            # Swap them
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 3: Reverse the suffix starting at i+1
        left, right = i+1, n-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
