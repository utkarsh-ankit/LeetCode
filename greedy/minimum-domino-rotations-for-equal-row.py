#class Solution:
    #def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # d={}
        # q={}
        # p=len(tops)
        # for i in tops:
        #     d[i]=tops.count(i)
        # for j in bottoms:
        #     q[j]=bottoms.count(j)
        # m=max(d.values())
        # n=max(q.values())
        # if m+n<p:
        #     return -1
        # if m>n:
        #     return p-m
        # return p-n
        # d={}
        # count=0
        # max_freq = 0
        # max_freq_key = None
        # a=tops.copy()
        # a.extend(bottoms)
        # p=len(tops)
        # for i in a:
        #     d[i]=a.count(i)
        # m=max(d.values())
        # for key, value in d.items():
        #     if value > max_freq:
        #         max_freq = value
        #         max_freq_key = key
        # k=max_freq_key
        # if m<p:
        #     return -1
        # for i in range(len(tops)):
        #     if tops[i]!=k and bottoms[i]!=k:
        #         return -1
        #         break
        #     elif tops[i]==k and bottoms[i]==k:
        #         continue
        #     count+=1
        # return count

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def rotations(x):
            top_rotations = bottom_rotations = 0
            for i in range(len(tops)):
                if tops[i] != x and bottoms[i] != x:
                    return float('inf')
                if tops[i] != x:
                    top_rotations += 1
                if bottoms[i] != x:
                    bottom_rotations += 1
            return min(top_rotations, bottom_rotations)
        
        res = min(rotations(tops[0]), rotations(bottoms[0]))
        return -1 if res == float('inf') else res





