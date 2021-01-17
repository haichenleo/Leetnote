# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# method1: 递归
class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # base case
        # 如果 l1/l2 为空，返回所有剩余节点，递归结束
        if not l1:
            return l2
        if not l2:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)

# method2: 迭代，头结点+双指针+尾插法
class Solution2:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        tail = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        # if not l1:
        #     tail.next = l2
        # else:
        #     tail.next = l1
        tail.next = l2 if not l1 else l1
        return dummy.next