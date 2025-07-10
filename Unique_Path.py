LeetCode Result:- https://leetcode.com/problems/unique-paths/submissions/1692607005

Example 1:
Input: m = 3, n = 7
Output: 28
Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Code
__________________________
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return self.comb(m + n - 2, m - 1)
    
    def comb(self, n, k):
        # compute n! / (k! * (n-k)!)
        if k > n - k:  # use symmetry
            k = n - k
        res = 1
        for i in range(1, k+1):
            res = res * (n - k + i) // i
        return res
