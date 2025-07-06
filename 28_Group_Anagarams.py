LeetCode Results:- https://leetcode.com/problems/group-anagrams/submissions/1688851819

"""Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other."""

Code
__________________________________________
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict

        anagrams = defaultdict(list)

        for word in strs:
            # sort the word to create the key
            key = ''.join(sorted(word))
            anagrams[key].append(word)

        return list(anagrams.values())
