class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(l,r,i):
            if l==n and r==n:
                res.append(i)
                return
            if l<n:
                dfs(l+1,r,i+"(")
            if r<l:
                dfs(l,r+1,i+")")
        dfs(0,0,"")
        return res
        