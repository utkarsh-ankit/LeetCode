class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        total = 0
        window_sum = 0

        for right in range(n):
            window_sum += nums[right]
            
            # While score is not valid, move left
            while window_sum * (right - left + 1) >= k:
                window_sum -= nums[left]
                left += 1

            total += right - left + 1  # all subarrays ending at right and starting between left and right

        return total
