import heapq
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        m = len(nums)
        n = m // 3

        # Prefix: smallest possible sum of n elements from left side
        left_sum = 0
        maxh = []
        pre = [0] * (m + 1)
        for i in range(2 * n):
            left_sum += nums[i]
            heapq.heappush(maxh, -nums[i])  # simulate max-heap
            if len(maxh) > n:
                left_sum += heapq.heappop(maxh)
            if len(maxh) == n:
                pre[i] = left_sum

        # Suffix: largest possible sum of n elements from right side
        right_sum = 0
        minh = []
        suf = [0] * (m + 1)
        for i in range(m - 1, n - 1, -1):
            right_sum += nums[i]
            heapq.heappush(minh, nums[i])
            if len(minh) > n:
                right_sum -= heapq.heappop(minh)
            if len(minh) == n:
                suf[i] = right_sum

        # Evaluate min difference for every valid split
        ans = float('inf')
        for i in range(n, 2 * n + 1):
            ans = min(ans, pre[i - 1] - suf[i])
        return ans

        