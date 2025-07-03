"""Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]"""

"""Go step by step for deeper understaing"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        Reverses nodes of a linked list in groups of size k.

        :param head: ListNode — Head of the linked list
        :param k: int — Size of the group to reverse
        :return: ListNode — Head of the modified linked list

        Algorithm:
        - Iterate the list and reverse every consecutive k nodes.
        - If the remaining nodes are fewer than k, leave them as-is.
        - Uses O(1) extra space and O(n) time.
        """
        # Dummy node simplifies edge case handling (like reversing first group)
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while True:
            # Find the k-th node from group_prev
            kth = self.get_kth_node(group_prev, k)
            if not kth:
                break  # less than k nodes left
            group_next = kth.next  # node after the k-th

            # Reverse the group
            prev = group_next
            curr = group_prev.next

            # Reverse current k nodes
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            # Connect previous part with newly reversed group
            tmp = group_prev.next  # store current group's head (will become tail)
            group_prev.next = kth  # point to new head
            group_prev = tmp       # move group_prev to the tail of the reversed group

        return dummy.next

    def get_kth_node(self, curr, k):
        """
        Helper function to find the k-th node from current node.

        :param curr: ListNode — start node
        :param k: int — number of steps forward
        :return: ListNode or None — k-th node or None if not enough nodes
        """
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
