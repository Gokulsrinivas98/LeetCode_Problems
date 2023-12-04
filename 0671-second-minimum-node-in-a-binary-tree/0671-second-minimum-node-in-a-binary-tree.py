# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def load(root, l):
            if not root:
                return
            load(root.left,l)
            l.append(root.val)
            load(root.right,l)
        l = []
        load(root,l)
        l_set = list(set(l))
        l_set.sort()
        if len(l_set) > 1:
            return l_set[1]  # Second minimum value
        else:
            return -1 