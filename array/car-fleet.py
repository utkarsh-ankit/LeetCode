class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        a=0
        fleet=0
        t=[]
        for i in range(len(position)):
            t.append((target-position[i])/speed[i])
        m=list(zip(position, speed, t))
        m=sorted(m, key=lambda x:x[0])                    #thing to revise
        
        for i in range(len(m)-1, -1, -1):
            if m[i][2]>a:
                fleet+=1
                a=m[i][2]
        return fleet


        