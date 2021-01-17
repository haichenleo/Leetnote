# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 数组+双指针
class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        # return vals == vals[::-1]
        # 双指针，向中间移动
        i, j = 0, len(vals)-1
        while i < j:
            if vals[i] != vals[j]:
                return False
            i += 1
            j -= 1
        return True

# 快慢指针
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        # 快慢指针找中间点
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # 如果fast不为空，说明节点有奇数个，此时slow在正中间，需要向后移动一位
        if fast:
            slow = slow.next
        # 旋转slow之后的链表
        tmp = slow
        slow = self.reverse(slow)
        # fast指向head，开始比较链表
        fast = head
        while slow:
            if fast.val != slow.val:
                return False
            slow = slow.next
            fast = fast.next
        # 恢复被反转的链表
        tmp = self.reverse(tmp)
        return True


    # 反转链表
    def reverse(self, head):
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev

class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        last = prev = None
        # 在快慢指针移动的过程中同时旋转前半部分的链表
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
            last.next = prev
            prev = last
        # 记录前后两端链表头
        prev_head = last
        post_head = slow
        # 处理奇数情况
        while fast:
            slow = slow.next
        # 对比两段链表
        while slow:
            if slow.val != last.val:
                return False
            slow = slow.next
            last = last.next
        # 恢复链表，先反转前部分链表
        self.reverse(prev_head)
        prev_head.next = post_head
        return True

    def reverse(self, head):
        prev, curr = None, head
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return prev
        