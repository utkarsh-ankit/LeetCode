class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        t=set(nums)
        for i in t:
            if i<k:
                return -1
            elif i==k:
                return len(t)-1
        else:
            return len(t)


        