class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # a=0
        # for i in range(len(nums1)):
        #     for j in range(len(nums2)):
        #         a ^= nums1[i]^nums2[j]
        # return a

#-------------------------------------------

        # a=0
        # b=0      
        # for i in nums1:
        #     a^=i
        # for j in nums2:
        #     b^=j
        # return a^b
        
#----------------------------------

        xor1 = 0 if len(nums2) % 2 == 0 else reduce(lambda x, y: x ^ y, nums1, 0)
        xor2 = 0 if len(nums1) % 2 == 0 else reduce(lambda x, y: x ^ y, nums2, 0)
        return xor1 ^ xor2     
