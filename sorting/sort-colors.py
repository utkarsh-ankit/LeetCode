from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        a,b,c=0,0,0
        for i in nums:
            if i==0:
                a+=1
            elif i==1:
                b+=1
            elif i==2:
                c+=1
        
        i=0
        for _ in range(a):
            nums[i]=0
            i+=1
        for _ in range(b):
            nums[i]=1
            i+=1
        for _ in range(c):
            nums[i]=2
            i+=1
        


        