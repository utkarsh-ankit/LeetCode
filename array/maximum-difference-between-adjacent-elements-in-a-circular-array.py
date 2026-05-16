class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        a=[abs(nums[i-1]-nums[i]) for i in range(len(nums))]
        a.append(abs(nums[0]-nums[len(nums)-1]))
        return max(a)
        