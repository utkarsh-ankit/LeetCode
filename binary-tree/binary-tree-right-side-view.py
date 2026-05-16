# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        view=[]
        def dfsr(node, depth):
            if not node:
                return
            
            if depth==len(view):          #imp
                view.append(node.val)

            dfsr(node.right, depth+1)
            dfsr(node.left, depth+1)
        
        dfsr(root,0)
        return view



        