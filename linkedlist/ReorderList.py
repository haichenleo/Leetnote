from selfdefined.ListNode import ListNode

class Solution1:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        vec = list()
        curr = head
        while curr:
            vec.append(curr)
            curr = curr.next

        i, j = 0, len(vec)-1
        while i < j:
            vec[i].next = vec[j]
            i += 1
            if i == j:
                vec[j].next = None
                break
            vec[j].next = vec[i]
            j -= 1
        vec[i].next = None

class Solution2:
    def reorderList(self, head: ListNode) -> None:
        if not (head and head.next and head.next.next):
            return
        
        # dummy+快慢指针找中点，慢指针指向中点或左中点
        dummy = ListNode()
        dummy.next = head
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 断开中点，反转后半部分
        newHead = slow.next
        slow.next = None
        prev = None
        while newHead:
            tmp = newHead.next
            newHead.next = prev
            prev = newHead
            newHead = tmp
        
        # 合并链表
        curr1 = head
        curr2 = prev
        while curr1 and curr2:
            tmp1 = curr1.next
            curr1.next = curr2
            curr1 = tmp1
            tmp2 = curr2.next
            curr2.next = curr1
            curr2 = tmp2


# test
from selfdefined.SimpleLinkedList import SimpleLinkedList

head1 = SimpleLinkedList.generate([1,2,3,4])
head2 = SimpleLinkedList.generate([1,2,3,4,5])
Solution2().reorderList(head1)
Solution2().reorderList(head2)
SimpleLinkedList.print(head1)
SimpleLinkedList.print(head2)