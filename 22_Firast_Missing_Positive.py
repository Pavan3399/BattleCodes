LeetCode Result:- https://leetcode.com/problems/first-missing-positive/submissions/1688834836

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

code 
_____________________________________________________________
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                # Swap nums[i] with nums[nums[i]-1]
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        # After rearrangement
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
