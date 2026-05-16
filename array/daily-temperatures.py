class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        a=len(temperatures)
        b=[0]*a
        stack=[]
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:
                c=stack.pop()
                b[c]=i-c
            stack.append(i)                    
        return b
                



