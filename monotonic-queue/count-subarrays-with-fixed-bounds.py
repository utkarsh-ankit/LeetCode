class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0
        min_pos = max_pos = bad_pos = -1  # Initialize positions
        
        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                bad_pos = i  # Update invalid element position
            
            if num == minK:
                min_pos = i  # Update last minK position
            if num == maxK:
                max_pos = i  # Update last maxK position
            
            ans += max(0, min(min_pos, max_pos) - bad_pos)
        
        return ans
