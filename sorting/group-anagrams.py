class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # a={}
        # for i in strs:
        #     b=tuple(sorted(i))       #tuple is hashable (important concept while dealing with dict)
        #     if b in a.keys():
        #         a[b].append(i)
        #     else:
        #         a[b]=[i]
        # return list(a.values())



        a={}
        for i in strs:
            b=tuple(sorted(i))
            if b in a.keys():
                a[b].append(i)
            else:
                a[b]=[i]
        return list(a.values())




    


