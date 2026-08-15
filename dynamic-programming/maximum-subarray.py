class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        max_sum=float('-inf')

        for i in range(len(nums)):
            cur+=nums[i]
            max_sum=max(max_sum,cur)

            if cur<0:
                cur=0

        return max_sum