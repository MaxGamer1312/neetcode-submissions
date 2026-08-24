# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_prev_head = None
        prev_head = None
        while head != None:
            if prev_head:
                prev_head.next = prev_prev_head
            prev_prev_head = prev_head
            prev_head = head
            head = head.next
        if prev_head:
            prev_head.next = prev_prev_head
        return prev_head