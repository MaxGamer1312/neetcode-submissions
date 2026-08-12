# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hasVisited = set()
        currHead = head
        while currHead != None:
            if currHead.next in hasVisited:
                return True
            hasVisited.add(currHead)
            currHead = currHead.next
        return False