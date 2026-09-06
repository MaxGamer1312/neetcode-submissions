# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
            heights = [0, 0]
            for i, curr_node in enumerate([curr_node.left, curr_node.right]):
                if not curr_node:
                    continue
                temp_stack = [(curr_node, 1)]
                while temp_stack:
                    curr_node = temp_stack.pop()
                    if curr_node[0] and curr_node[0].left:
                        temp_stack.append((curr_node[0].left, curr_node[1]+1))
                    if curr_node[0] and curr_node[0].right:
                        temp_stack.append((curr_node[0].right, curr_node[1]+1))
                    if not temp_stack:
                        heights[i] = curr_node[1]
            if abs(heights[0]-heights[1]) > 1:
                return False
        return True
