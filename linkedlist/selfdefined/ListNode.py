class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        curr = self
        while curr:
            if curr.next:
                print(curr.val, '->', end='')
            else:
                print(curr.val)
            curr = curr.next