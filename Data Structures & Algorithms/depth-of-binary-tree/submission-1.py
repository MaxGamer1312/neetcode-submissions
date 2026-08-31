# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        visited = {
            None: 0,
            root: 1
        }
        stack = [(root, None)]
        max_depth = 0
        while stack:
            curr_node = stack.pop()
            curr_depth = 1+visited[curr_node[1]]
            visited[curr_node[0]] = curr_depth
            if curr_depth > max_depth:
                max_depth = curr_depth
            if curr_node[0].left:
                stack.append((curr_node[0].left, curr_node[0]))
            if curr_node[0].right:
                stack.append((curr_node[0].right, curr_node[0]))
        return max_depth