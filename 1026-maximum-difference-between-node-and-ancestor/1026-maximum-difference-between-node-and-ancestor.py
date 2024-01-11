# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, currMin, currMax):
            if node:
                self.res = max(self.res, node.val - currMin, currMax - node.val)
                currMin, currMax = min(node.val,currMin) , max(node.val, currMax)
                dfs(node.left,currMin,currMax)
                dfs(node.right,currMin,currMax)
        dfs(root,root.val,root.val)
        return self.res
    