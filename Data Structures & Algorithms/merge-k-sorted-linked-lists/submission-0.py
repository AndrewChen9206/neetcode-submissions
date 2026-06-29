# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        min_heap = []
        dummy_head = ListNode()
        pointer = dummy_head
        count = 0

        for head in lists:
            if not head:
                continue

            heapq.heappush(min_heap, (head.val, count, head))
            count += 1
        
        while min_heap:
            _, _, head = heapq.heappop(min_heap)
            pointer.next = head
            pointer = pointer.next

            if head.next:
                heapq.heappush(min_heap, (head.next.val, count, head.next))
                count += 1
        
        return dummy_head.next