# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        currHead = head
        while currHead != None:
            headNext = currHead.next
            currHead.next = prev
            prev = currHead
            if currHead:
                print(currHead.val)
                if currHead.next:
                    print(currHead.next.val)
            print("###")
            if headNext != None:
                currHead = headNext
            else:
                break
        
        return currHead
        