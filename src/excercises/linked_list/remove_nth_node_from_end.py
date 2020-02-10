# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    Input:
        The head of a linked list
        n: integer between 0 to the length of the list
        Return a linked list where the nth element from the end was removed.
    """
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l, r = head, head
        for _ in range(n):
            r = r.next
        if r is None:
            return head.next

        while r.next is not None:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head
