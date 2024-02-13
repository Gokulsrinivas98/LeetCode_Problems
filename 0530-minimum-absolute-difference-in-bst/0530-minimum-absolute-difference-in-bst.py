# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def absDif(node,lo,hi):
            
            if not node: return hi-lo
            left = absDif(node.left,lo,node.val)
            right = absDif(node.right,node.val,hi)
            return min(left,right)
        return absDif(root,(-2**31),(2**31-1))
            