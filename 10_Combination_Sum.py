Leetcode Result:- https://leetcode.com/problems/combination-sum/submissions/1685156234


Idea to breackdown the logic:
Use backtracking (DFS) to explore all possible combinations.
At each step, you can:
Pick the same number again (because reuse is allowed).
Or move to the next number.
Stop the recursion when:
The current sum > target → backtrack.
The current sum == target → record the combination.

Code Starts
__________________________________________________________________
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        
        def backtrack(start, path, total):
            if total == target:
                res.append(list(path))
                return
            if total > target:
                return
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])  # not i+1 because we can reuse same element
                path.pop()
        
        backtrack(0, [], 0)
        return res
