"""Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6"""

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        
        # initialize the heap with the head of each list
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, idx, node))
        
        dummy = ListNode(0)
        current = dummy
        
        while min_heap:
            val, idx, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, idx, node.next))
        
        return dummy.next
