LeetCode Result:- https://leetcode.com/problems/permutations-ii/submissions/1688847642

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

Code
_________________________________
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()  # sort to make it easy to skip duplicates

        def backtrack(path, visited):
            if len(path) == len(nums):
                res.append(list(path))
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                # skip duplicates: if the same number as previous and previous was not used
                if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
                    continue
                visited[i] = True
                backtrack(path + [nums[i]], visited)
                visited[i] = False

        backtrack([], [False] * len(nums))
        return res
