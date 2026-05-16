class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        minim=float('inf')
        diff=-1
        for i in range(len(nums)):
            minim=min(minim,nums[i])
            if minim==nums[i]:
                j=i+1
                while j in range(i+1,len(nums)):
                    if nums[j]>minim:
                        diff=max(diff, nums[j]-minim)
                    j+=1
        return diff


        