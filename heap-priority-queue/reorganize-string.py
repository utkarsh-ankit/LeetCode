class Solution:
    def reorganizeString(self, s:str)->str:
        # cnt = Counter(s)
        # maxH = [(-c, ch) for ch, c in cnt.items()]
        # heapq.heapify(maxH)
        # prev = None
        # res = ''

        # while prev or maxH:
        #     if prev and not maxH:
        #         return ''

        #     c, ch = heapq.heappop(maxH)
        #     res += ch
        #     c += 1

        #     if prev:
        #         heapq.heappush(maxH, prev)
        #         prev = None
        #     if c!=0:
        #         prev = (c, ch)

        # return res

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



