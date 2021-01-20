# 输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
# 输出：9 -> 1 -> 2，即912

from selfdefined.ListNode import ListNode


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        curr = None
        carry = 0
        while stack1 or stack2 or carry > 0:
            sum = carry
            sum += 0 if not stack1 else stack1.pop()
            sum += 0 if not stack2 else stack2.pop()
            node = ListNode(sum % 10)
            carry = sum // 10
            node.next = curr
            curr = node
        return curr


# test
from selfdefined.SimpleLinkedList import SimpleLinkedList

l1 = SimpleLinkedList.generate([6,1,7])
l2 = SimpleLinkedList.generate([2,9,5])
res = Solution().addTwoNumbers(l1,l2)
SimpleLinkedList.print(res)
