class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        a = set()
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(0, i - k), min(len(nums), i + k + 1)):
                    a.add(j)
        return sorted(a)
