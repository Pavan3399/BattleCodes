LeetCode Result:- https://leetcode.com/problems/edit-distance/submissions/1694641589

"""Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')"""

COde
______________________________
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m, n = len(word1), len(word2)

        # Create DP table (m+1) x (n+1)
        dp = [[0] * (n+1) for _ in range(m+1)]

        # Initialize first row and first column
        for i in range(m+1):
            dp[i][0] = i  # delete all characters
        for j in range(n+1):
            dp[0][j] = j  # insert all characters

        # Fill DP table
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # delete
                        dp[i][j-1],    # insert
                        dp[i-1][j-1]   # replace
                    )

        return dp[m][n]
