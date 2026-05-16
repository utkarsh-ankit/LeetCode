class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # a={nums1[i]:i for i in range(len(nums1))}
        # result=[-1]*len(nums1)

        # for i in range(len(nums2)):
        #     if nums2[i] in a:
        #         t=i+1
        #         while t<len(nums2):
        #             if nums2[t]>nums2[i]:
        #                 result[a[nums2[i]]]=nums2[t]
        #                 break
        #             t+=1
        
        # return result

        a={nums1[i]:i for i in range(len(nums1))}
        result=[-1]*len(nums1)     
        stack=[]

        for i in range(len(nums2)):
            cur=nums2[i]
            while stack and cur>stack[-1]:
                value=stack.pop()
                indx=a[value]
                result[indx]=cur
            if cur in a:
                stack.append(cur)
        return result


        

        