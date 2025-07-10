LeetCode Result:- https://leetcode.com/problems/rotate-list/submissions/1692603155

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]

Code
_____________________
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head
        
        # Find the length of the list and the tail node
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        # Normalize k
        k %= length
        if k == 0:
            return head
        
        # Make the list circular
        tail.next = head
        
        # Find new tail: (length - k - 1) steps from head
        steps_to_new_tail = length - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next
        
        # Break the circle and set new head
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head
