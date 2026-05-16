class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # l=0
        # r=len(nums)-1
        # zeros=-1
        
        # while l<=r:
        #     mid=(l+r)//2
        #     if nums[mid]==0:
        #         zeros=mid
        #         r=mid-1
        #     elif nums[mid]<0:
        #         l=mid+1
        #     else:
        #         r=mid-1
        # return zeros



        if nums[0] > 0:  # All positive
            return len(nums)
        if nums[-1] < 0:  # All negative
            return len(nums)

        l, r = 0, len(nums) - 1
        first_zero_index = -1  

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == 0:
                first_zero_index = mid  # Found zero, but look left for first occurrence
                r = mid - 1  
            elif nums[mid] < 0:
                l = mid + 1  
            else:
                r = mid - 1  

        # **Fix: Count negatives correctly**
        negative_count = first_zero_index if first_zero_index != -1 else l

        # **Fix: Find the first positive number**
        l, r = 0, len(nums) - 1
        first_positive_index = len(nums)  # Default to len(nums) if no positive numbers exist
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > 0:
                first_positive_index = mid  # Found a positive, but look left for first occurrence
                r = mid - 1  
            else:
                l = mid + 1  

        positive_count = len(nums) - first_positive_index  # **Count elements after first positive**

        return max(negative_count, positive_count)


        