# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_length = 0
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
            max_length = max(max_length, self.check_depth(curr_node))
        return max_length

    def check_depth(self, current_node):
        if not root:
            return 0
        visited = {
            None: 0,
            root: 1
        }
        max_depth_left = 0
        if current_node.left:
            stack = [(current_node.left, None)]
            while stack:
                curr_node = stack.pop()
                curr_depth = 1+visited[curr_node[1]]
                visited[curr_node[0]] = curr_depth
                if curr_depth > max_depth_left:
                    max_depth_left = curr_depth
                if curr_node[0].left:
                    stack.append((curr_node[0].left, curr_node[0]))
                if curr_node[0].right:
                    stack.append((curr_node[0].right, curr_node[0]))
        max_depth_right = 0
        if current_node.right:
            stack = [(current_node.right, None)]
            while stack:
                curr_node = stack.pop()
                curr_depth = 1+visited[curr_node[1]]
                visited[curr_node[0]] = curr_depth
                if curr_depth > max_depth_right:
                    max_depth_right = curr_depth
                if curr_node[0].left:
                    stack.append((curr_node[0].left, curr_node[0]))
                if curr_node[0].right:
                    stack.append((curr_node[0].right, curr_node[0]))
        return max_depth_left+max_depth_right