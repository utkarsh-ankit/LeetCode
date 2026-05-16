from itertools import permutations
from typing import List

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        valid_numbers = set()
        
        # Generate every ordered choice of 3 digits (respects available counts)
        for h, t, u in permutations(digits, 3):
            if h == 0:                  # no leading zeros
                continue
            if u % 2 != 0:             # must be even
                continue
            
            num = 100*h + 10*t + u
            valid_numbers.add(num)
        
        # Return sorted list of unique valid numbers
        return sorted(valid_numbers)
