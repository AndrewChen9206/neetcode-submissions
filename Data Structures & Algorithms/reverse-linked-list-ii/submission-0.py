# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(next=head)
        pre = dummy

        for _ in range(left - 1):
            pre = pre.next
            
        curr = pre.next
        prev = None

        for _ in range(right-left+1):
            temp_node = curr.next
            curr.next = prev
            prev = curr
            curr = temp_node
        
        pre.next.next = curr
        pre.next = prev

        return dummy.next