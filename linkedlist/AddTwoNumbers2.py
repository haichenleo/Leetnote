from selfdefined.ListNode import ListNode

class Solution:
    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = list()
        stack2 = list()
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        last = None
        while stack1 or stack2 or carry > 0:
            sum = carry
            sum += 0 if len(stack1) == 0 else stack1.pop()
            sum += 0 if len(stack2) == 0 else stack2.pop()
            node = ListNode(sum % 10)
            node.next = last
            last = node
            carry = sum // 10
        return last

# Test
from selfdefined.SimpleLinkedList import SimpleLinkedList

l1 = SimpleLinkedList.generate([7,2,4,3])
l2 = SimpleLinkedList.generate([5,6,4])
res = Solution().addTwoNumbers2(l1,l2)
SimpleLinkedList.print(res)