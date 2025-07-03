Leetcode Results:- https://leetcode.com/problems/count-and-say/submissions/1685148782

Please go thorught step by step for better understanding.
Code starts
________________________________________________
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"
        for _ in range(1, n):
            result = self.next_seq(result)
        return result
    
    def next_seq(self, s):
        count = 1
        result = []
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count))
                result.append(s[i - 1])
                count = 1
        # append last run
        result.append(str(count))
        result.append(s[-1])
        return "".join(result)
