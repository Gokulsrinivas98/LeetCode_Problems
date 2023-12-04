# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        def appender(root,l):
            if not root:
                return
            appender(root.left,l)
            l.append(root.val)
            appender(root.right,l)
            
        l = []
        appender(root,l)
        l.sort()
        return l[k-1]