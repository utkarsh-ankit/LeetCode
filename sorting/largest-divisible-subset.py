class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        nums.sort()
        n = len(nums)
        dp = [[] for _ in range(n)]  # dp[i] = largest divisible subset ending at i

        for i in range(n):
            max_subset = []
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) > len(max_subset):
                    max_subset = dp[j]
            dp[i] = max_subset + [nums[i]]

        return max(dp, key=len)



        