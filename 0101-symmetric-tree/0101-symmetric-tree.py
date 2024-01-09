# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(left,right):
            if left and right and left.val == right.val:
                return mirror(left.right,right.left) and mirror(left.left, right.right)
            return left == right
        return not root or mirror(root.left,root.right)