# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            curr_node = stack.pop()
            if curr_node.left:
                stack.append(curr_node.left)
            if curr_node.right:
                stack.append(curr_node.right)
            temp_curr_node = curr_node
            subtree_stack = [subRoot]
            temp_stack = [curr_node]
            while temp_stack and subtree_stack:
                temp_curr_node = temp_stack.pop()
                temp_subtree_node = subtree_stack.pop()
                if temp_curr_node.left:
                    temp_stack.append(temp_curr_node.left)
                if temp_curr_node.right:
                    temp_stack.append(temp_curr_node.right)
                if temp_subtree_node.left:
                    subtree_stack.append(temp_subtree_node.left)
                if temp_subtree_node.right:
                    subtree_stack.append(temp_subtree_node.right)
                if temp_curr_node.val != temp_subtree_node.val:
                    break
                else:
                    if not temp_stack and not subtree_stack:
                        return True
        return False