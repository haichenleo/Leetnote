from selfdefined.ListNode import ListNode

class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cache = {head.val}
        prev = head
        while prev.next:
            curr = prev.next
            if curr.val not in cache:
                cache.add(curr.val)
                prev = prev.next
            else:
                prev.next = prev.next.next
        return head


# test
from selfdefined.SimpleLinkedList import SimpleLinkedList

head = SimpleLinkedList.generate([1,2,3,2,3,1])
res = Solution().removeDuplicateNodes(head)
res.printNode()


            
                

