# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr = head
        prev = None
        for _ in range(length//2):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if length % 2 == 0:
            prev_prev = None
        else: 
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            prev_prev = prev
            temp_prev_prev = prev_prev.next
            prev_prev.next = None
            prev = temp_prev_prev
        while curr:
            temp_curr = curr.next
            curr.next = prev_prev
            temp_prev = prev.next
            prev.next = curr
            prev_prev = prev

            prev = temp_prev
            curr = temp_curr

        

