class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # r=nums1+nums2
        # r.sort()
        # if len(r)%2==0:
        #     return (r[(len(r)//2)-1]+r[(len(r)//2)])/2
        # else:
        #     return (r[((len(r)+1)//2)-1])

        return median(sorted(nums1+nums2))

        