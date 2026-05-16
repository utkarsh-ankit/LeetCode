class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        p=[]
        i=0
        while i<len(nums):
            if nums[i+1]-nums[i]>k or nums[i+2]-nums[i]>k:
                return []
            p.append([nums[i],nums[i+1],nums[i+2]])
            i+=3
        return p

            
            
        