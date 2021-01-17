from selfdefined.ListNode import ListNode

class SimpleLinkedList:

    # def __init__(self, nums: list) -> None:
    #     self.dummy = ListNode()
    #     self.generate(nums)

    @staticmethod
    def generate(nums: list) -> ListNode:
        dummy = curr = ListNode()
        for n in nums:
            curr.next = ListNode(n)
            curr = curr.next
        return dummy.next

    @staticmethod
    def print(head: ListNode):
        while head:
            if head.next:
                print(head.val, '->', end='')
            else:
                print(head.val)
            head = head.next