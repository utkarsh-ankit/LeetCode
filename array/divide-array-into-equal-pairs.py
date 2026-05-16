class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        # nums.sort()
        # if len(nums)%2==1:
        #     return False
        # while nums:
        #     t=nums.pop()
        #     if t!=nums[-1]:
        #         return False
        #     nums.pop()
        # return True




        # k={i:nums.count(i) for i in nums}         
        # for key, value in k.items():
        #     if value%2==1:
        #         return False
        # return True


        
        freq=Counter(nums)
        return all(value%2==0 for value in freq.values())
                
        