from typing import List

class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        m, n = len(grid), len(grid[0])
        max_kills = 0
        
        # col_counts[j] will hold the number of enemies in the current vertical segment for column j
        col_counts = [0] * n
        
        for i in range(m):
            row_count = 0  # number of enemies in the current horizontal segment
            for j in range(n):
                # Recompute row_count at the start of a new segment
                if j == 0 or grid[i][j-1] == 'W':
                    row_count = 0
                    k = j
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_count += 1
                        k += 1
                
                # Recompute col_counts[j] at the start of a new segment
                if i == 0 or grid[i-1][j] == 'W':
                    col_counts[j] = 0
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_counts[j] += 1
                        k += 1
                
                # If this cell is empty, it's a valid bomb placement
                if grid[i][j] == '0':
                    # Total enemies killed = row hits + column hits
                    total = row_count + col_counts[j]
                    if total > max_kills:
                        max_kills = total
        
        return max_kills
