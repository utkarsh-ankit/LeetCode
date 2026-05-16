class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-2):
            if nums[i]==0:
                count+=1
                for k in range(i,i+3):
                    nums[k] ^= 1
        if nums[-1]==0 or nums[-2]==0:
            return -1

        return count
            