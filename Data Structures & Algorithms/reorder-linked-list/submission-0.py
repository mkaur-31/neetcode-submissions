# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next : return None

        prev , curr = None, head
        while curr:
            curr.prev = prev
            prev = curr
            curr = curr.next

        head1, head2 = head, prev

        while head1.next != head2 and head1 != head2:
            _head2 = head2.prev
            head2.next = head1.next
            head1.next = head2
            
            head1 = head2.next
            head2 = _head2
        head2.next = None
        