from typing import List

class BIT:
    def __init__(self, size):
        self.tree = [0] * (size + 2)
        self.size = size + 2

    def update(self, i, delta):
        i += 1
        while i < self.size:
            self.tree[i] += delta
            i += (i & -i)

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res += self.tree[i]
            i -= (i & -i)
        return res

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        # Step 1: Map values in nums2 to their indices
        pos_in_nums2 = [0] * n
        for i, v in enumerate(nums2):
            pos_in_nums2[v] = i

        # Step 2: Transform nums1 to positions in nums2
        transformed = [pos_in_nums2[v] for v in nums1]

        # Step 3: Count how many valid x for each y (left counts)
        bit_left = BIT(n)
        left_count = [0] * n
        for i in range(n):
            left_count[i] = bit_left.query(transformed[i] - 1)
            bit_left.update(transformed[i], 1)

        # Step 4: Count how many valid z for each y (right counts)
        bit_right = BIT(n)
        right_count = [0] * n
        for i in reversed(range(n)):
            right_count[i] = bit_right.query(n - 1) - bit_right.query(transformed[i])
            bit_right.update(transformed[i], 1)

        # Step 5: For each index i, count good triplets with y = nums1[i]
        total = 0
        for l, r in zip(left_count, right_count):
            total += l * r

        return total

        