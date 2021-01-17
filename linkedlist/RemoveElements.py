# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            # 如果删除节点，prev不动
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            # 无论是否删除，curr指针向后移动
            curr = curr.next
        return dummy.next

class Solution2:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        # base case，递归边界
        if not head:
            return None
        head.next = self.removeElements(head.next)
        if head.val == val:
            return head.next
        else:
            return head