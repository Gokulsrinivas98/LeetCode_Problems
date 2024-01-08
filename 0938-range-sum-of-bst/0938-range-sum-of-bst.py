# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def rangesum(node):
            if not node: return 0 
            count = 0
            if low <= node.val <= high:
                count += node.val
            if node.val > low:
                count += rangesum(node.left)
            if node.val < high:
                count += rangesum(node.right)
            
            return count
        
        return rangesum(root)
    
        