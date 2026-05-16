class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x: x[0])  # Sort by start day
        k = 0

        if not meetings:
            return days

        if meetings[0][0] > 1:
            k += meetings[0][0] - 1

        last_end = meetings[0][1]

        for i in range(1, len(meetings)):
            if meetings[i][0] > last_end + 1:
                k += meetings[i][0] - (last_end + 1)
            last_end = max(last_end, meetings[i][1])

        k += days - last_end

        return k
        