# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        fast_curr = head
        while curr != None and fast_curr != None:
            curr = curr.next
            fast_curr = fast_curr.next
            if not fast_curr:
                return False
            fast_curr = fast_curr.next 
            if curr != None and curr == fast_curr:
                return True
        return False