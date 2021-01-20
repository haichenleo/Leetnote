from selfdefined.ListNode import ListNode

# 哈希表 + 列表排序
class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        cache = dict()
        curr = head
        arr = []
        while curr:
            if curr.val in cache:
                cache[curr.val] += 1
            else:
                cache[curr.val] = 1
            curr = curr.next
        for key in cache:
            if cache[key] == 1:
                arr.append(key)
        arr = sorted(arr)
        dummy = ListNode(-1)
        prev = dummy
        for val in arr:
            node = ListNode(val)
            prev.next = node
            prev = prev.next
        return dummy.next

# 双指针
class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        dummy = ListNode()
        dummy.next = head
        prev, curr = dummy, head
        while curr and curr.next:
            if curr.val != curr.next.val:
                prev = prev.next
            else:
                while curr.next and curr.val == curr.next.val:
                    curr = curr.next
                prev.next = curr.next
            curr = curr.next
        return dummy.next

    
# test
from selfdefined.SimpleLinkedList import SimpleLinkedList
head = SimpleLinkedList.generate([1,2,3,3,4,4,5])
res = Solution2().deleteDuplicates(head)
res.printNode()

        