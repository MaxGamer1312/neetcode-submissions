# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        if not list1:
            return list2
        if not list2:
            return list1
        newList = ListNode()
        newL1 = list1
        newL2 = list2
        if newL1.val < newL2.val:
            tempL1 = ListNode()
            tempL1.val = newL1.val
            newList = tempL1
            newL1 = newL1.next
        else:
            tempL2 = ListNode()
            tempL2.val = newL2.val
            newList = tempL2
            newL2 = newL2.next
        newListHead = newList
        while newL1 and newL2:
            if newL1.val < newL2.val:
                tempL1 = ListNode()
                tempL1.val = newL1.val
                newList.next = tempL1
                newL1 = newL1.next
            else:
                tempL2 = ListNode()
                tempL2.val = newL2.val
                newList.next = tempL2
                newL2 = newL2.next
            newList = newList.next
        if newL1:
            newList.next = newL1
        else:
            newList.next = newL2
        return newListHead 