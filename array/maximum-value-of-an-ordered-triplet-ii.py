class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        # t=0
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums)):
        #             t=max(t, (nums[i]-nums[j])*nums[k])
        # return t

        # t=0
        # i=nums[0]
        # for j in range(1, len(nums)-1):
        #     if i<nums[j]:
        #         i=nums[j]
        #     for k in range(j+1, len(nums)):
        #         t=max(t, (i-nums[j])*nums[k])
        # return t

        prefix_max=nums[0]
        max_diff=0
        t=0

        for i in range(1, len(nums)):
            t=max(t, max_diff*nums[i])
            prefix_max=max(prefix_max, nums[i])
            max_diff=max(max_diff, prefix_max-nums[i])
        return t





        