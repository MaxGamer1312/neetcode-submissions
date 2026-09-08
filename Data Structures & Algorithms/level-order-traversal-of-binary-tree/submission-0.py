# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        curr_stack = [root]
        next_stack = []
        while True:
            curr_result = []
            while curr_stack:
                curr_node = curr_stack.pop(0)
                curr_result.append(curr_node.val)
                if curr_node.left:
                    next_stack.append(curr_node.left)
                if curr_node.right:
                    next_stack.append(curr_node.right)
            result.append(curr_result)
            if not next_stack:
                break
            curr_stack = next_stack
            next_stack = []
            
        return result