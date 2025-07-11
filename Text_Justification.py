LeetCode Result:- https://leetcode.com/problems/text-justification/submissions/1694636208

"""Example 1:
Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:
Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
Note that the second line is also left-justified because it contains only one word.
Example 3:
Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]"""

Code
________________________
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        i = 0
        n = len(words)

        while i < n:
            # figure out how many words fit in this line
            line_len = len(words[i])
            j = i + 1
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            # now words[i:j] are in this line
            line_words = words[i:j]
            spaces_needed = maxWidth - sum(len(w) for w in line_words)

            # if it's the last line or only one word in the line
            if j == n or len(line_words) == 1:
                line = ' '.join(line_words) + ' ' * (maxWidth - len(' '.join(line_words)))
            else:
                # distribute spaces
                gaps = len(line_words) - 1
                space_per_gap = spaces_needed // gaps
                extra_spaces = spaces_needed % gaps

                line = ''
                for k in range(gaps):
                    line += line_words[k]
                    line += ' ' * (space_per_gap + (1 if k < extra_spaces else 0))
                line += line_words[-1]  # last word in the line

            res.append(line)
            i = j

        return res
