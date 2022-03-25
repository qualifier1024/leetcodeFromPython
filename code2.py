# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"2"


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        resHead = resNode = ListNode()
        tens = units = num = 0
        while tens or l1 or l2:
            num = (l1.val if l1 else 0) + (l2.val if l2 else 0) + tens
            tens, units = num // 10, num % 10
            resNode.next = ListNode(units)
            resNode, l1, l2 = resNode.next, l1.next if l1 else None, l2.next if l2 else None
        return resHead.next
