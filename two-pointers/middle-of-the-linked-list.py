# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        if head.next.next is None:
            return head.next
        else:
            fast=head
            slow=head
            while head:
                slow=slow.next
                fast=fast.next.next
                if fast.next==None:
                    return slow
                elif fast.next.next==None:
                    return slow.next
            
        