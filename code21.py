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


def list_to_listnode(lst):
    dummy = ListNode()
    cur = dummy
    for val in lst:
        cur.next = ListNode(val)
        cur = cur.next
    return dummy.next


def listnode_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res


if __name__ == "__main__":
    solution = Solution()
    list1 = list_to_listnode([1,2,4])
    list2 = list_to_listnode([1,3,4])
    result = solution.mergeTwoLists(list1, list2)
    print(listnode_to_list(result))