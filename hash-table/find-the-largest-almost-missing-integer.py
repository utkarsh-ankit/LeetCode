# class Solution:
#     def largestInteger(self, nums: List[int], k: int) -> int:
#         hmap={i:0 for i in nums}

#         for i in range(len(nums)-k+1):
#             for j in range(i, i+k):
#                 hmap[nums[j]]+=1

#         freq=min(hmap.values())

#         c=[key for key, value in hmap.items() if value==freq]

#         if len(set(hmap.values()))==1:
#             return -1

#         return max(c)


class Solution:
    def largestInteger(self, nums, k):
        hmap = {num: 0 for num in nums}

        n = len(nums)
        for i in range(n - k + 1):
            distinct_vals = set(nums[i : i + k])
            for val in distinct_vals:
                hmap[val] += 1

        c = [key for key, count in hmap.items() if count == 1]

        return max(c) if c else -1

        
                
        