from selfdefined.ListNode import ListNode


class Solution:
    def splitListToParts(self, root: ListNode, k: int):
        smallHead = small = ListNode()
        largeHead = large = ListNode()
        while root:
            if root.val < k:
                small.next = root
                small = small.next
            else:
                large.next = root
                large = large.next
            root = root.next
        # 切断原节点的指针
        large.next = None
        small.next = largeHead.next
        return smallHead.next


# test
from selfdefined.SimpleLinkedList import SimpleLinkedList
root = SimpleLinkedList.generate([1,4,3,2,5,2])
res = Solution().splitListToParts(root, 3)
SimpleLinkedList.print(res)