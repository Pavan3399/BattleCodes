Leetcode Aesult:- https://leetcode.com/problems/combination-sum-ii/submissions/1685161721

Breaking down the logic code for better understanding:
->Sort the candidates first.
->Backtrack through the sorted list.
->At each step:
->Either include the current number and move to the next.
->Or skip it.
->If you see the same number as previous at the same level, skip it to avoid duplicates.

Code starts
______________________________________________
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        res = []
        
        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue  # skip duplicates
                
                path.append(candidates[i])
                backtrack(i+1, path, total + candidates[i])  # move to next index (no reuse)
                path.pop()
        
        backtrack(0, [], 0)
        return res
