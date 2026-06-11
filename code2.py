class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


"""
2. Add Two Numbers / 两数相加 (Medium)

给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。
请你将两个数相加，并以相同形式返回一个表示和的链表。
你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""


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


if __name__ == "__main__":
    solution = Solution()
    print("Example 1:", listnode_to_list(solution.addTwoNumbers(
        list_to_listnode([2, 4, 3]), list_to_listnode([5, 6, 4]))))   # Expected: [7, 0, 8]
    print("Example 2:", listnode_to_list(solution.addTwoNumbers(
        list_to_listnode([0]), list_to_listnode([0]))))               # Expected: [0]
    print("Example 3:", listnode_to_list(solution.addTwoNumbers(
        list_to_listnode([9, 9, 9, 9, 9, 9, 9]), list_to_listnode([9, 9, 9, 9]))))  # Expected: [8,9,9,9,0,0,0,1]
