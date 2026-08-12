# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        nodeList = [root]
        while nodeList:
            currNode = nodeList.pop(0)
            if currNode.left:
                nodeList.append(currNode.left)
            if currNode.right:
                nodeList.append(currNode.right)

            temp = currNode.left
            currNode.left = currNode.right
            currNode.right = temp
        return root