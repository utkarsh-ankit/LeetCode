# class Solution:
#     def bubble_sort(self, a):
#         n = len(a)
#         for i in range(n):  # Multiple passes
#             for j in range(0, n-i-1):  # Compare adjacent elements
#                 if a[j] > a[j+1]:  # Swap if out of order
#                     a[j], a[j+1] = a[j+1], a[j]
#         return a
    
#     def remove_duplicates(self, k):
#         if not k:  # Handle empty list edge case
#             return []
#         t=[k[0]]

#         for i in range(len(k)-1):
#             if k[i]!=k[i+1]:
#                 t.append(k[i+1])
#         return t

#     def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         nums1=self.bubble_sort(nums1)
#         nums2=self.bubble_sort(nums2)
#         nums1=self.remove_duplicates(nums1)
#         nums2=self.remove_duplicates(nums2)

#         o=[]
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i]==nums2[j]:
#                     o.append(nums1[i])
#         return o



from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert both lists to sets to remove duplicates and allow fast lookup
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection of the two sets
        result = set1.intersection(set2)
        
        # Convert the set back to a list as the output requires a list
        return list(result)
