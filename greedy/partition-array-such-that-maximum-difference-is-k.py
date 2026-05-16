class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        nums.sort()
        count = 1
        group_start = nums[0]
        
        for x in nums:
            # if adding x would violate the max−min ≤ k constraint,
            # start a new subsequence at x
            if x - group_start > k:
                count += 1
                group_start = x
        
        return count
