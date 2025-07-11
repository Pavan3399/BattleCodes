LeetCode Result:- https://leetcode.com/problems/simplify-path/submissions/1694637850

"""Example 1:
Input: path = "/home/"
Output: "/home"
Explanation:
The trailing slash should be removed."""

Code
_________________________
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(part)

        return '/' + '/'.join(stack)
