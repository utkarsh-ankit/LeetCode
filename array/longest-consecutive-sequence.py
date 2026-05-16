class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a=0
        # f=0
        # nums.sort()
        # if len(nums)==0:
        #     return 0
        # for i in range(1,len(nums)):
        #     if nums[i]-nums[i-1]==1:
        #         f+=1
        #     elif nums[i]==nums[i-1]:
        #         continue
        #     else:
        #         f=0
        #     a=max(f,a)
        # return a+1

        b=set(nums)
        a=0
        for i in b:
            if i-1 not in b:
                lengt=1
                f=i
                while f+1 in b:
                    f+=1
                    lengt+=1
                else:
                    f=0
                a=max(lengt,a)
        return a


        