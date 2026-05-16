class Solution:
    def maximumValueSum(self, nums: List[int], k: int, edges: List[List[int]]) -> int:
        total = 0
        cnt_toggled = 0
        min_diff = float('inf')
        
        for x in nums:
            toggled = x ^ k
            # Pick the better of original or toggled
            total += max(x, toggled)
            # Count if we chose toggled
            if toggled > x:
                cnt_toggled += 1
            # Track the smallest absolute difference
            min_diff = min(min_diff, abs(x - toggled))
        
        # If we have an odd number of toggles, remove the smallest gain
        if cnt_toggled % 2 == 1:
            total -= min_diff
        
        return total
