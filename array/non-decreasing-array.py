class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        k=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                k+=1
                if k>1:
                    return False

                if i > 0 and nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
        return True


        