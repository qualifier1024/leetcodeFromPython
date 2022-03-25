"1"


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val<list2.val:
                res=list1
                list1 = list1.next
            else:
                res =list2
                list2=list2.next
        else:
            return list1 if list1 else list2
        res.next=self.mergeTwoLists(list1,list2)
        return res