class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        # Greedy helper: count how many pairs we can form with differences ≤ maxDiff
        def count_pairs(maxDiff: int) -> int:
            cnt = 0
            i = 0
            n = len(nums)
            while i + 1 < n:
                if nums[i+1] - nums[i] <= maxDiff:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt

        low, high = 0, nums[-1] - nums[0]
        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) >= p:
                high = mid
            else:
                low = mid + 1
        return low

        