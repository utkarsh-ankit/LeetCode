# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # r=[]
        # def dfs(root,k):
        #     if k>0:
        #         if root.left:
        #             dfs(root.left,k) 
        #         r.append(root.val)
        #         k-=1
        #         if root.right:
        #             dfs(root.right,k)
        # dfs(root,k)
        # return r[k-1]

        m=0
        def dfs(root):
            nonlocal k, m
            if not root:
                return
            dfs(root.left) 
            k-=1
            if k==0:
                m=root.val
                return
            dfs(root.right)
        dfs(root)
        return m

            

# - from root, if we count the left of the root and compare it with the k, we can know if it exist left or right of the k
# -something like inorder traversal can help
#- it can also be solved by the heap



        