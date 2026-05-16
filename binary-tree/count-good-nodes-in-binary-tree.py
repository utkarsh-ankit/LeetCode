# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        a=float("-inf")
        gn=0
        def dfs(node, a):
            nonlocal gn
            if not node:
                return
            if a<=node.val:
                gn+=1
                a=max(a, node.val)
            dfs(node.left, a)
            dfs(node.right, a)
        dfs(root, a)
        return gn
        


        