class Solution:
    # def maximumCandies(self, candies: List[int], k: int) -> int:
    #     if sum(candies)<k:
    #         return 0
        
    #     t=min(candies)
    #     p=[i%t for i in candies]
    #     q=[j//t for j in candies]

    #     for m in range(len(candies)):
    #         while candies[m]>t:
    #             if candies[m]-p[m]>0 and q[m]>=1:
    #                 candies[m]=candies[m]-p[m]
    #                 candies.append(p[m])
    #             if candies[m]-p[m]==0 and q[m]>1:
    #                 candies[m]=candies[m]-t
    #                 candies.append(t)
        
    #     maxsize=0
        
    #     for x in range(1, max(candies)+1):
    #         pieces=sum(candy//x for candy in candies)
    #         if pieces>=k:
    #             maxsize=x
        
    #     return maxsize


    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:  # ✅ If we can't even distribute k candies, return 0
            return 0

        # ✅ Binary search range: from 1 to max(candies)
        left, right = 1, max(candies)
        best = 0  # ✅ Store best possible max piece size
        
        while left <= right:
            mid = (left + right) // 2  # ✅ Mid represents a possible piece size
            pieces = sum(candy // mid for candy in candies)  # ✅ Count total pieces we can form

            if pieces >= k:
                best = mid  # ✅ Valid size, try larger pieces
                left = mid + 1
            else:
                right = mid - 1  # ✅ Reduce size to fit condition
        
        return best  # ✅ Return the maximum valid piece size



                

        
        