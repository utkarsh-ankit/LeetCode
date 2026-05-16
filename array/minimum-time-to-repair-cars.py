class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right=1, min(ranks)*(cars**2)

        def ct(t):
            total_cars=0
            for i in ranks:
                max_cars=int((t/i)**0.5)
                total_cars+=max_cars
                if total_cars>=cars:
                    return True
            return False

        while left<right:
            mid=(left+right)//2
            if ct(mid):
                right=mid
            else:
                left=mid+1
            
        return left


        