class Solution:
    def reorganizeString(self, s:str)->str:

        count=Counter(s)

        if max(count.values())>((len(s)+1)//2):
            return ""
        
        max_count=[(-co, ch) for ch, co in count.items()]

        heapq.heapify(max_count)

        string=""
        prev=None

        while max_count:
            co,ch= heapq.heappop(max_count)
            
            if ch==prev:
                co2,ch2= heapq.heappop(max_count)
                string+=ch2
                co2+=1
                if co2!=0:
                    heapq.heappush(max_count, (co2,ch2))
                heapq.heappush(max_count, (co,ch))
            else:
                string+=ch
                co+=1
                if co!=0:
                    heapq.heappush(max_count, (co,ch))
            prev=string[-1]

        return string



