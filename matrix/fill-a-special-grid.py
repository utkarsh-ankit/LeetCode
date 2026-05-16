from typing import List

class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        def build(n, start):
            if n == 0:
                return [[start]]

            size = 2 ** (n - 1)
            area = size * size

            # Recursively construct quadrants
            top_right = build(n - 1, start)
            bottom_right = build(n - 1, start + area)
            bottom_left = build(n - 1, start + 2 * area)
            top_left = build(n - 1, start + 3 * area)

            grid = [[0] * (2 * size) for _ in range(2 * size)]

            for i in range(size):
                for j in range(size):
                    grid[i][j] = top_left[i][j]                 # Top-left
                    grid[i][j + size] = top_right[i][j]         # Top-right
                    grid[i + size][j + size] = bottom_right[i][j]  # Bottom-right
                    grid[i + size][j] = bottom_left[i][j]       # Bottom-left

            return grid

        return build(N,0)
