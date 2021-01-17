# k个一组反转链表

class ListNode:
    def __init__(self, val) -> None:
        self.val = val
        self.next = next

# Method1：递归反转子区间
class Solution1:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        start = end = head
        # 如果区间长度不足k，不反转直接返回
        for _ in range(k):
            if not end:
                return head
            end = end.next
        # 反转[start, end)
        new_head = self.reverse(head, end)
        # 头指针指向下个区间的返回值
        start.next = self.reverseKGroup(end, k)
        return new_head
        
    # 反转区间[start, end)
    def reverse(self, start: ListNode, end: ListNode):
        if not (start and start.next):
            return start
        prev, curr = None, start
        while curr is not end:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# Method2:
class Solution1:
    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        # 辅助头结点
        dummy = ListNode(0)
        dummy.next = head
        # prev指向反转区间头结点的前一个节点，end指向反转区间的尾结点
        prev = end = dummy
        # 迭代，
        while end.next:
            # 移动k次end，判断是否为空
            i = 0
            while i < k and end:
                end = end.next
                i += 1
            if not end: break  # 移动后end可能为空
            tmp = end.next
            end.next = None
            start = prev.next
            prev.next = self.reverse(start)
            start.next = tmp
            prev = end = start
        return dummy.next

    
    # 反转链表
    def reverse(self, start: ListNode):
        if not (start and start.next):
            return start
        prev, curr = None, start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev