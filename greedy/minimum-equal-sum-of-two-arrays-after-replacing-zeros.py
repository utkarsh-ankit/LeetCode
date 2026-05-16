class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        count1=0
        count2=0
        for i in nums1:
            if i==0:
                count1+=1
        for i in nums2:
            if i==0:
                count2+=1 
        a=sum(nums1)
        b=sum(nums2)
        t=abs(a-b)
        if (count1==0 and count2+b>a) or (count2==0 and count1+a>b):
            return -1
        return max(a+count1, b+count2)
        

