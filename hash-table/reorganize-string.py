import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        t=[]
        y={i:s.count(i) for i in s}
        if max(y.values()) > (sum(y.values())-max(y.values()))+1:
            return ""

        for char, freq in y.items():
            heapq.heappush(t, (-freq, char))

        result = []
        prev_freq, prev_char = 0, ""

        while t:
            freq, char = heapq.heappop(t)
            result.append(char)

            if prev_freq<0:
                heapq.heappush(t, (prev_freq, prev_char))

            prev_freq=freq+1
            prev_char=char

        return "".join(result)

            





            
        