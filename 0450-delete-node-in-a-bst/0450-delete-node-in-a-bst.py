# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        if root is None:
            return root
        
        if key < root.val:
            root.left = self.deleteNode(root.left,key)
        elif key > root.val:
            root.right = self.deleteNode(root.right,key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            successor = self.findSuccessor(root.right)
            root.val = successor.val
            root.right = self.deleteNode(root.right,successor.val)
        return root
    
    def findSuccessor(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current