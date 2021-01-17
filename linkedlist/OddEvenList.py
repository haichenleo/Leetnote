# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 方法一：
class Solution1:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # 头尾指针
        oddHead = oddTail = head
        evenHead = evenTail = head.next
        # 每轮循环各调整一次尾指针，偶数链表尾指针始终指向下一未访问节点或null，避免出现环
        while evenTail and evenTail.next:
            oddTail.next = evenTail.next
            oddTail = oddTail.next
            evenTail.next = oddTail.next
            evenTail = evenTail.next
        oddTail.next = evenHead
        return oddHead

# 方法二：虚拟头结点+奇偶标识符
class Solution2:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        # 虚拟头节点、尾指针
        oddHead = oddTail = ListNode()
        evenHead = evenTail = ListNode()
        isOdd = True
        curr = head
        # 根据奇偶性判断选用哪个尾指针，利用尾插法插入节点
        while curr:
            if isOdd:
                oddTail.next = curr
                oddTail = curr
            else:
                evenTail.next = curr
                evenTail = curr
            isOdd = not isOdd  # 改变奇偶性flag
            curr = curr.next   # 移动指针
        # 奇数尾指针指向偶数头结点
        oddTail.next = evenHead.next
        # ！当节点数为奇数个时，如 1 -> 2 -> 3 -> null，循环结束后2仍指向3，形成了环
        # 需要将偶链表的next设为null
        evenTail.next = None
        return oddHead.next