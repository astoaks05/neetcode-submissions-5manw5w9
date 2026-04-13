# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        if head.next is None:
            return head
        
        cur = head
        prev = None
        next = cur.next

        cur.next = prev
        while next:
            prev = cur
            cur = next
            next = next.next
            cur.next = prev
        
        return cur

        