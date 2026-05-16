class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a=1
        n=len(nums)
        t=0
        r=1
        for i in nums:
            a*=i
        if a!=0:
            return [a//i for i in nums]               #brute force
        elif nums.count(0)>1:
            return [0]*n
        else:
            t = nums.index(0)
            r = 1
            for x in nums:
                if x != 0:
                    r *= x
            res = [0] * n
            res[t] = r
            return res