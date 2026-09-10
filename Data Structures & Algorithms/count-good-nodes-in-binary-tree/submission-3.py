# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack = [(root, root.val)]
        good_node_counter = 0
        while stack:
            curr_node = stack.pop()
            if curr_node[0].val >= curr_node[1]:
                good_node_counter += 1
            if curr_node[0].left:
                stack.append((curr_node[0].left, max(curr_node[0].val, curr_node[1])))
            if curr_node[0].right:
                stack.append((curr_node[0].right, max(curr_node[0].val, curr_node[1])))
        return good_node_counter
            
            