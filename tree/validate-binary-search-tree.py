# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # if not root:
        #     return True
        # if root.left and root.val>root.left.val:
        #     self.isValidBST(root.left)
        # if root.right and root.val<root.right.val:
        #     self.isValidBST(root.right)
        # return False
        
        def dfs(node, l, h):
            if not node:
                return True
            if not (l<node.val<h):
                return False
            return dfs(node.left, l, node.val) and dfs(node.right, node.val, h)

        return dfs(root, float("-inf"), float("inf"))

        