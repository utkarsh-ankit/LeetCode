class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        d = [0] * (n+1)
        # mark each range [l, r] in the diff array
        for l, r in queries:
            d[l] += 1
            d[r+1] -= 1

        # apply the prefix sums and check as we go
        curr = 0
        for i, x in enumerate(nums):
            curr += d[i]
            if x > curr:      # not enough decrements available
                return False
        return True
