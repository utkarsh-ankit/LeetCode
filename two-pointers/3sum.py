from typing import List

class Solution:
    def threeSum(self, k: List[int]) -> List[List[int]]:
        res=[]
        k.sort()

        for i,a in enumerate(k):
            if i>0 and a==k[i-1]:
                continue
            
            l,r = i+1, len(k)-1
            while l<r:
                t=a+k[l]+k[r]
                if t>0:
                    r-=1
                elif t<0:
                    l+=1
                else:
                    res.append([a,k[l],k[r]])
                    l+=1
                    while k[l]==k[l-1] and l<r:
                        l+=1
        return res
