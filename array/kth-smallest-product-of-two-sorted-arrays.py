from bisect import bisect_right, bisect_left

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def count_le(x):
            cnt = 0
            j1, j2 = len(nums2) - 1, 0
            for a in nums1:
                if a > 0:
                    # want b <= x/a
                    cnt += bisect_right(nums2, x // a)
                elif a < 0:
                    # want b >= ceil(x/a)
                    cnt += len(nums2) - bisect_left(nums2, -((-x) // a))
                else:
                    # a == 0, product is 0
                    if x >= 0:
                        cnt += len(nums2)
            return cnt

        left, right = -10**10, 10**10
        while left < right:
            mid = (left + right) // 2
            if count_le(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

        