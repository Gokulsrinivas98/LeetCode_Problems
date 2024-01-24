# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        hashset = set()
        ans = 0 
        
        def check(node,hashset):
            nonlocal ans
            if not node: return
            if node.val in hashset: hashset.remove(node.val)
            else: hashset.add(node.val)
            
            if not node.left and not node.right:
                if len(hashset) <= 1: ans += 1
            
            check(node.left,hashset.copy())
            check(node.right,hashset.copy())
         
        check(root,hashset)
        return ans
    