from typing import List

class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_cut(intervals):
            # Sort intervals by start
            intervals.sort()
            m = len(intervals)

            # If less than 3 rectangles, can't make 3 non-empty sections
            if m < 3:
                return False
            
            # Prefix max of end points
            prefix_max = [0] * m
            prefix_max[0] = intervals[0][1]
            for i in range(1, m):
                prefix_max[i] = max(prefix_max[i-1], intervals[i][1])

            # Suffix min of start points
            suffix_min = [0] * m
            suffix_min[-1] = intervals[-1][0]
            for i in range(m-2, -1, -1):
                suffix_min[i] = min(suffix_min[i+1], intervals[i][0])

            # Try all valid first and second cut points
            for i in range(m - 2):
                if prefix_max[i] <= suffix_min[i + 1]:
                    for j in range(i + 1, m - 1):
                        if prefix_max[j] <= suffix_min[j + 1]:
                            return True
            return False

        # Try vertical cuts (x-intervals)
        x_intervals = [(x1, x2) for x1, y1, x2, y2 in rectangles]
        if can_cut(x_intervals):
            return True

        # Try horizontal cuts (y-intervals)
        y_intervals = [(y1, y2) for x1, y1, x2, y2 in rectangles]
        if can_cut(y_intervals):
            return True

        return False
