class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        a=[]
        for i in range(len(code)-1, -1, -1):
            if isActive[i] is False:
                isActive.pop(i)
                businessLine.pop(i)
                code.pop(i)
        for i in range(len(code)-1, -1, -1):
            if businessLine[i] not in ["electronics", "grocery", "pharmacy", "restaurant"]:
                isActive.pop(i)
                businessLine.pop(i)
                code.pop(i)
        for i in range(len(code)-1, -1, -1):
            if not code[i] or not all(c.isalnum() or c == '_' for c in code[i]):
                isActive.pop(i)
                businessLine.pop(i)
                code.pop(i)

        o = {"electronics":0, "grocery":1, "pharmacy":2, "restaurant":3}
        for t,l in zip(businessLine, code):
            a.append((o[t],t,l))
        a.sort(key=lambda e:(e[0],e[2]))
        b=[]
        
        for i,j,c in a:
            b.append(c)
        return b
            
        
        
                
                
                
        
        