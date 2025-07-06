LeetCode Result:- https://leetcode.com/problems/multiply-strings/submissions/1688838636

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Code
______________________________________
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        # result can have at most m + n digits
        result = [0] * (m + n)

        # multiply each digit
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                sum_ = mul + result[i + j + 1]

                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10

        # skip leading zeros
        res = []
        for num in result:
            if not (len(res) == 0 and num == 0):
                res.append(str(num))

        return ''.join(res)
