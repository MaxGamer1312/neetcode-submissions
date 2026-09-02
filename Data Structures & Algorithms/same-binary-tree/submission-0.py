# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if p or q:
                return False
            return True
        stack_p = [p]
        stack_q = [q]
        while stack_p and stack_q:
            curr_p = stack_p.pop()
            curr_q = stack_q.pop()
            if curr_p.val != curr_q.val:
                return False
            if curr_p.left or curr_q.left:
                if not curr_p.left or not curr_q.left:
                    return False
                stack_p.append(curr_p.left)
                stack_q.append(curr_q.left)
            if curr_p.right or curr_q.right:
                if not curr_p.right or not curr_q.right:
                    return False
                stack_p.append(curr_p.right)
                stack_q.append(curr_q.right)
        if not stack_p and not stack_q:
            return True
        return False