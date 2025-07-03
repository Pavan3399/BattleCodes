leetcode Result:- https://leetcode.com/problems/regular-expression-matching/submissions/1685216622


"""Example 1:
Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa"."""


Code start
______________________________________
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Initialize dp for patterns like a*, a*b*, a*b*c* that can match empty string
        for j in range(2, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                    dp[i][j] = dp[i][j-2]  # zero occurrence
                    if p[j-2] == '.' or p[j-2] == s[i-1]:
                        dp[i][j] |= dp[i-1][j]  # one or more occurrence

        return dp[m][n]
        
