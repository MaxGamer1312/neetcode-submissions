# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result_head = None
        result_curr = result_head
        result_prev = None
        l1_curr = l1
        l2_curr = l2
        prev_quotient = 0
        while l1_curr or l2_curr:
            l1_val = 0
            l2_val = 0
            if l1_curr:
                l1_val = l1_curr.val
                l1_curr = l1_curr.next
            if l2_curr:
                l2_val = l2_curr.val
                l2_curr = l2_curr.next
            total = l1_val+l2_val+prev_quotient
            prev_quotient = total // 10
            curr_remainder = total % 10
            result_curr = ListNode(curr_remainder)
            if not result_prev:
                result_head = result_curr
            else:
                result_prev.next = result_curr
            result_prev = result_curr
        if prev_quotient > 0:
            result_curr.next = ListNode(prev_quotient)

        return result_head