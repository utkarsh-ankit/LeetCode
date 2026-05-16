from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # a=[]
        # for i in nums:
        #     t=0
        #     for j in nums:
        #         if i==j:
        #             t+=1
        #     if (i,t) not in a:
        #         a.append((i,t))
        # l=sorted(a, key=lambda x: x[1], reverse=True)
        # return [item[0] for item in l[:k]]

        a={i:nums.count(i) for i in set(nums)}
        sorted_items = sorted(a.items(), key=lambda x: x[1], reverse=True)

        return [item[0] for item in sorted_items[:k]]


