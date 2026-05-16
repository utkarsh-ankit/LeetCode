class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)
        mh=[-c for c in count.values()]
        heapq.heapify(mh)

        time = 0
        q=deque()

        while mh or q:
            time+=1

            if mh:
                cnt=1+heapq.heappop(mh)
                if cnt:
                    q.append([cnt, time+n])

            if q and q[0][1]==time:
                    heapq.heappush(mh, q.popleft()[0])

        return time