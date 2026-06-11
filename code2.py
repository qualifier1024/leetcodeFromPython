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


if __name__ == "__main__":
    solution = Solution()
    l1 = list_to_listnode([2, 4, 3])
    l2 = list_to_listnode([5, 6, 4])
    result = solution.addTwoNumbers(l1, l2)
    print(listnode_to_list(result))