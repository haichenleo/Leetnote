# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

from selfdefined.ListNode import ListNode


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head:
            return None
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        
        # 将prev移动m-1次，prev的下一个节点为m 
        i = 1
        while i < m:
            prev = prev.next
            i += 1
        curr = prev.next
        post, tail = prev, curr  # 记录prev、curr的位置，控制反转后的指针
        # 此时 i = m
        while i <= n:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            i += 1
        post.next = prev
        tail.next = curr

        return dummy.next




# test
from selfdefined.SimpleLinkedList import SimpleLinkedList
head = SimpleLinkedList.generate([1,2,3,4,5])
res = Solution().reverseBetween(head,2,4)
res.printNode()