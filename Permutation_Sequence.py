Leetcode Results:- https://leetcode.com/problems/permutation-sequence/submissions/1692588447

Example 1:
Input: n = 3, k = 3
Output: "213"
Example 2:
Input: n = 4, k = 9
Output: "2314"
Example 3:
Input: n = 3, k = 1
Output: "123"


code
_______________________
class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        from math import factorial

        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # convert to 0-based index
        result = []

        for i in range(n, 0, -1):
            fact = factorial(i - 1)
            index = k // fact
            result.append(numbers.pop(index))
            k %= fact

        return ''.join(result)
