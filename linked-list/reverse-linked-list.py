# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        prev=None
        temp=head
        while temp:
            new=temp.next
            temp.next=prev
            prev=temp
            temp=new
        head=prev
   
        return head

        