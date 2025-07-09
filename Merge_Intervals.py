LeetCode Result:- https://leetcode.com/problems/merge-intervals/submissions/1691477077

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Code
______________________
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if not intervals:
            return []
        
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        for interval in intervals:
            # if merged is empty or there is no overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # there is overlap, merge intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged
