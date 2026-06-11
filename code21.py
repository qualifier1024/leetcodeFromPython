"""
21. Merge Two Sorted Lists / 合并两个有序链表 (Easy)

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:
Input: list1 = [], list2 = []
Output: []

Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
"""


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
    print("Example 1:", listnode_to_list(solution.mergeTwoLists(
        list_to_listnode([1,2,4]), list_to_listnode([1,3,4]))))  # Expected: [1,1,2,3,4,4]
    print("Example 2:", listnode_to_list(solution.mergeTwoLists(
        list_to_listnode([]), list_to_listnode([]))))            # Expected: []
    print("Example 3:", listnode_to_list(solution.mergeTwoLists(
        list_to_listnode([]), list_to_listnode([0]))))           # Expected: [0]
