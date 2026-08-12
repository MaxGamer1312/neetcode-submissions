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
        currTree = [root]
        count = 0
        while currTree:
            newCurrTree = []
            for currNode in currTree:
                if currNode.left:
                    newCurrTree.append(currNode.left)
                if currNode.right:
                    newCurrTree.append(currNode.right)
            currTree = newCurrTree
            count+=1
        return count