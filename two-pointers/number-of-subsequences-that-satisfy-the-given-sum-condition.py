class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()
        n = len(nums)
        pow2 = [1] * n
        for i in range(1, n):
            pow2[i] = (pow2[i-1] * 2) % MOD

        res = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                res = (res + pow2[right - left]) % MOD
                left += 1

        return res
