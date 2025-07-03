"""Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation:
The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words."""

"""Please go through Step by Step for better understanding"""

class Solution(object):
    def findSubstring(self, s, words):
        """
        Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once.
        
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count
        n = len(s)
        word_map = Counter(words)
        res = []

        for i in range(word_len):  # we need to try all possible offsets: 0..word_len-1
            left = i
            count = 0
            seen = {}
            for j in range(i, n - word_len + 1, word_len):
                word = s[j:j + word_len]
                if word in word_map:
                    seen[word] = seen.get(word, 0) + 1
                    count += 1

                    # If seen too many of this word, move left forward
                    while seen[word] > word_map[word]:
                        left_word = s[left:left + word_len]
                        seen[left_word] -= 1
                        left += word_len
                        count -= 1

                    # If all words matched
                    if count == word_count:
                        res.append(left)
                else:
                    # reset window
                    seen.clear()
                    count = 0
                    left = j + word_len
        return res
