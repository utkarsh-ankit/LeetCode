class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        h_m2 = {}
        for i in range(len(s)):
            if s[i] not in h_m2:
                h_m2[s[i]] = [i]
                for j in range(len(s)-1, i-1, -1):
                    if s[i] == s[j]:
                        h_m2[s[i]].append(j)
                        break

                if len(h_m2[s[i]]) == 1:
                    h_m2[s[i]].append(h_m2[s[i]][0])

        sorted_chars = sorted(h_m2.keys(), key=lambda x: h_m2[x][0])
        res = []
        if not sorted_chars:
            return res
            
        start = h_m2[sorted_chars[0]][0]
        end = h_m2[sorted_chars[0]][1]
        
        for i in range(1, len(sorted_chars)):
            current_start = h_m2[sorted_chars[i]][0]
            current_end = h_m2[sorted_chars[i]][1]
            if current_start < end:
                end = max(end, current_end)
            else:
                res.append(end - start + 1)
                start = current_start
                end = current_end

        res.append(end - start + 1)
        return res