# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, float("inf"), float("-inf"))]
        while stack:
            curr_node = stack.pop()
            if curr_node[0].left:
                min_left = curr_node[0].val
                if curr_node[0].left.val >= min_left or curr_node[0].left.val <= curr_node[2]:
                    return False
                stack.append((curr_node[0].left, min_left, curr_node[2]))
            if curr_node[0].right:
                max_right = curr_node[0].val
                if curr_node[0].right.val <= max_right or curr_node[0].right.val >= curr_node[1]:
                    return False
                stack.append((curr_node[0].right, curr_node[1], max_right))
        return True
            