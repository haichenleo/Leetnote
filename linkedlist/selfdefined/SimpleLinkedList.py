from selfdefined.ListNode import ListNode

class SimpleLinkedList:

    def __init__(self, nums: list) -> None:
        self.dummy = ListNode()
        self.generate(nums)

    def generate(self, nums: list) -> ListNode:
        if not nums:
            return None
        curr = self.dummy
        for n in nums:
            node = ListNode(n)
            curr.next = node
            curr = curr.next

    # def print(self):
    #     curr = self.dummy.next
    #     while curr:
    #         if curr.next:
    #             print(curr.val, '->', end='')
    #         else:
    #             print(curr.val)
    #         curr = curr.next