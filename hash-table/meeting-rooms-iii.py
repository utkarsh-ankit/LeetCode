import heapq

class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meetings.sort()
        used_rooms = []
        available_rooms = list(range(n))
        heapq.heapify(available_rooms)
        count = [0] * n

        for start, end in meetings:
            # Free up rooms that have ended before the current meeting starts
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heapq.heappop(used_rooms)
                heapq.heappush(available_rooms, room)
            
            duration = end - start
            if available_rooms:
                room = heapq.heappop(available_rooms)
                heapq.heappush(used_rooms, (end, room))
                count[room] += 1
            else:
                end_time, room = heapq.heappop(used_rooms)
                heapq.heappush(used_rooms, (end_time + duration, room))
                count[room] += 1

        max_meetings = max(count)
        for i in range(n):
            if count[i] == max_meetings:
                return i
