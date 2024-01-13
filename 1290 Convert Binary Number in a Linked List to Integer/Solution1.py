class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        pointer = head
        res = 0
        while pointer != None:
            res = res * 2 + pointer.val
            pointer = pointer.next
        return res