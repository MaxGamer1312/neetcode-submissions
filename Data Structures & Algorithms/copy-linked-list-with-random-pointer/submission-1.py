"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new_dict = {
            None: None
        }
        curr = head
        new_curr = None
        prev_new_curr = None
        while curr:
            if curr in old_to_new_dict:
                new_curr = old_to_new_dict[curr]
            else:
                new_curr = Node(curr.val)
                old_to_new_dict[curr] = new_curr
            if curr.random not in old_to_new_dict:
                old_to_new_dict[curr.random] = Node(curr.random.val)
            new_curr.random = old_to_new_dict[curr.random]
            if prev_new_curr:
                prev_new_curr.next = new_curr
            curr = curr.next
            prev_new_curr = new_curr
        return old_to_new_dict[head]
