from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Step 1: Flatten the grid into a list
        flat = [num for row in grid for num in row]
        
        # Step 2: Check if all values mod x are the same (feasibility check)
        base_mod = flat[0] % x
        for num in flat:
            if num % x != base_mod:
                return -1  # Impossible to make all values equal
        
        # Step 3: Sort the flattened list to find the median
        flat.sort()
        median = flat[len(flat) // 2]
        
        # Step 4: Calculate total number of operations to convert all values to median
        operations = sum(abs(num - median) // x for num in flat)
        
        return operations
