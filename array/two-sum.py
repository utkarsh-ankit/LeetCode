class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={nums[j]:j for j in range(len(nums))}
        for i in range(len(nums)):
            if target-nums[i] in dict1 and dict1[target-nums[i]]!=i:    #the order of these 2 logic matters
                return [i, dict1[target-nums[i]]]

        



