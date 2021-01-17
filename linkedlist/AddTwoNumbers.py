# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = curr = ListNode()
        carry = 0  # 进位值
        while l1 or l2:
            n1 = l1.val if l1 else 0  # 较短链表空缺的节点值视为0
            n2 = l2.val if l2 else 0
            summary = n1 + n2 + carry
            curr.next = ListNode(summary % 10)
            carry = summary // 10
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:    
                l2 = l2.next
        if carry != 0:
            curr.next = ListNode(carry)
        return dummy.next
