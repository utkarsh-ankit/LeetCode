class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=[]
        
        def dfs(i,k):

            if i>=len(nums):
                res.append(k)
                return

            k=k^nums[i]
            dfs(i+1,k)

            k=k^nums[i]
            dfs(i+1,k)
            k=k^nums[i]

        dfs(0,0)
        return sum(res)
            
