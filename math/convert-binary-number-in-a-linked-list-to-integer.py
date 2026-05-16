class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        result = 0
        node = head
        while node:
            result = (result << 1) | node.val
            node = node.next
        return result
