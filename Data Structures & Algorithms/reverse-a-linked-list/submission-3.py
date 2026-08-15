# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        result_head = ListNode()
        result = result_head
        normal_list = []
        while head:
            normal_list.append(head.val)
            head = head.next
        for i in range(len(normal_list) - 1, 0, -1):
            result.val = normal_list[i]
            result.next = ListNode()
            result = result.next
        result.val = normal_list[0]
        return result_head