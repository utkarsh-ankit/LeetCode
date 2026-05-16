# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        def sam(a,b):
            if not a and not b:
                return True
            if not a or not b:
                return False
            if a.val==b.val:
                i=sam(a.left, b.left)
                j=sam(a.right, b.right)
                return i and j
            return False

        if root.val==subRoot.val and sam(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) #check the tree other parts, keeping the subtree same

        


        