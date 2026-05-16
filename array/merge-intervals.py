class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out=[intervals[0]]

        for start, end in intervals[1:]:
            lastend=out[-1][1]

            if start<=lastend:
                out[-1][1]=max(lastend, end)
            else:
                out.append([start, end])
        return out
        