from collections import defaultdict

class Solution:
    def countInterestingSubarrays(self, nums: List[int], mod: int, k: int) -> int:
        counter = defaultdict(int)
        counter[0] = 1
        prefix = 0
        ans = 0       
        for num in nums:
            if num % mod == k:
                prefix += 1
            ans += counter[(prefix - k) % mod]            
            counter[prefix % mod] += 1       
        return ans
