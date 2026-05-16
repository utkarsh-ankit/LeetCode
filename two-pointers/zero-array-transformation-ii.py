class Solution:
    # def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
    #     if all(num == 0 for num in nums):
    #         return 0
    #     count=0
    #     for i in range(len(queries)):
    #         for j in range(queries[i][0], queries[i][1]+1):
    #             nums[j] = max(nums[j] - queries[i][2], 0)
    #         count+=1
    #         if all(num == 0 for num in nums):
    #             return count
    #     return -1

    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        if all(num == 0 for num in nums):
            return 0
        n = len(nums)
        m = len(queries)
        
        # Helper function: given k queries (first k in order),
        # check if for each index, the total allowed decrement is >= nums[i].
        def can_zero(k: int) -> bool:
            diff = [0] * (n + 1)  # difference array of length n+1
            # Apply first k queries using the difference array technique
            for j in range(k):
                l, r, val = queries[j]
                diff[l] += val
                if r + 1 < n:
                    diff[r + 1] -= val
            
            # Compute prefix sum and check condition for each index.
            running = 0
            for i in range(n):
                running += diff[i]
                # If the allowed decrement is less than needed, return False.
                if running < nums[i]:
                    return False
            return True
        
        # Binary search for the minimal k in the range [1, m]
        low, high = 1, m + 1  # high is exclusive upper bound
        ans = -1
        while low < high:
            mid = (low + high) // 2
            if can_zero(mid):
                ans = mid
                high = mid  # try to find a smaller k
            else:
                low = mid + 1
        
        return ans if ans != -1 else -1



                



        