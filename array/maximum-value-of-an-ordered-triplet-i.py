class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        t=0
        l=nums[0]
        for j in range(1, len(nums)-1):
            if nums[j]>l:
                l=nums[j]
            for k in range(j+1, len(nums)):
                t=max(t,(l-nums[j])*nums[k])
        return t




        