# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        stack = [root]
        while stack:
            curr_element = stack.pop()
            temp = curr_element.left
            curr_element.left = curr_element.right
            curr_element.right = temp
            if curr_element.left:
                stack.append(curr_element.left)
            if curr_element.right:
                stack.append(curr_element.right)
        return root