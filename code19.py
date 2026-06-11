"""
19. Remove Nth Node From End of List / 删除链表的倒数第 N 个结点 (Medium)

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
"""


from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next


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
    head = list_to_listnode([1,2,3,4,5])
    result = solution.removeNthFromEnd(head, 2)
    print(listnode_to_list(result))