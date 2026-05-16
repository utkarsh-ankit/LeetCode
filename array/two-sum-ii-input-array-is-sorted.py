class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i]+numbers[j]==target:
        #             return [i+1, j+1]

        for i in range(len(numbers)):
            k=target-numbers[i]
            l,h=i+1,len(numbers)-1

            while l<=h:
                mid=(l+h)//2
                if numbers[mid]==k:
                    return[i+1, mid+1]
                elif numbers[mid]<k:
                    l=mid+1
                else:
                    h=mid-1
        return []


        