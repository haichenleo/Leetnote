from selfdefined.ListNode import ListNode

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        pA, pB = headA, headB
        while pA is not pB:
            if pA == None:
                pA = headB
            if pB == None:
                pB = headA
            pA = pA.next
            pB = pB.next
        return pA



# test
# from selfdefined.SimpleLinkedList import SimpleLinkedList

# headA = SimpleLinkedList.generate([4,1,8,4,5])
# headB = SimpleLinkedList.generate([5,0,1,8,4,5])
# res = Solution().getIntersectionNode(headA,headB)
# res.printNode()