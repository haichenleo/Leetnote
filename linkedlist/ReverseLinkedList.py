# 1.反转链表
# https://leetcode-cn.com/problems/reverse-linked-list/


class ListNode:
    def __init__(self, x) -> None:
        self.val = x
        self.next = None

# method1 - 迭代
def reverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head
    while curr:
        prev, curr, curr.next = curr, curr.next, prev
    return prev

# method2 - 递归
def reverseList2(self, head: ListNode) -> ListNode:
    # 终止条件，递归到尾节点返回 tail
    if not head or not head.next:
        return head

    # 后序遍历 - 先递归到tail，再操作节点
    # 尾结点head.next为空，返回tail本身
    # 其他节点最后一行继续返回传递这个尾结点，故函数最后返回tail
    tail = reverseList2(head.next)

    # 操作除tail之外的节点
    head.next.next = head  # 让下一个节点指向当前节点
    head.next = None       # 当前节点指向空

    # 传递尾结点
    return tail

# 2.反转前N个节点

def reverseN(self, head: ListNode, n: int) -> ListNode:

    # 后区节点
    successor = None
    # 递归到最后一个需要反转的节点，用successor记录它的下一个节点
    if n == 1:
        successor = head.next
        return head
    # 后序遍历，n-1
    tail = reverseN(head.next, n-1)
    # 节点操作，
    head.next.next = head
    head.next = successor
    return tail