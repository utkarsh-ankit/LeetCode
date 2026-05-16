class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        px=[]
        py=[]
        s=set()
        
        v=1
        while v<bound:
            px.append(v)
            if x==1:
                break
            v=v*x #v*=x

        v=1
        while v<bound:
            py.append(v)
            if y==1:
                break
            v=v*y
        
        for i in px:
            for j in py:
                t=i+j
                if t<=bound:
                    s.add(t)
        
        return list(s)


                

        