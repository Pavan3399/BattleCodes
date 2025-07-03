Leetcode result:- https://leetcode.com/problems/longest-valid-parentheses/submissions/1685119011

"""Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"."""

class Solution(object):
    def longestValidParentheses(self, s):
        """
        Find length of longest valid parentheses substring.
        
        :type s: str
        :rtype: int
        """
        stack = [-1]  # stack to hold indices, start with -1 as base
        max_len = 0
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:  # char == ')'
                stack.pop()
                if not stack:
                    stack.append(i)  # new base when stack is empty
                else:
                    max_len = max(max_len, i - stack[-1])
        
        return max_len
