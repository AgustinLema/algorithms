# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        previous = None
        while current is not None:
            nx_node = current.next
            current.next = previous
            previous = current
            current = nx_node
        return previous


class Solution2:
    """
    Iterative solution
    """
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        root = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return root
