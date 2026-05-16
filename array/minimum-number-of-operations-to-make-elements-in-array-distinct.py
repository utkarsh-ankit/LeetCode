class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        a=set(nums)
        count=0
        if len(nums)==len(a):
            return count
        for n in range(3,len(nums),3):
            count+=1
            a=set(nums[n:])
            if len(nums[n:])==len(a) and len(nums[n:])>3:
                break
        if len(nums[count*3:]) != len(set(nums[count*3:])):
            count += 1
        return count


        

        