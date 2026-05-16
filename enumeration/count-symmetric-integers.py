class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count=0
        for i in range(low, high+1):
            t=str(i)
            if len(t)%2!=0:
                continue
            k=len(t)//2
            if sum(map(int,t[:k]))==sum(map(int,t[k:])):
                count+=1
            else:
                continue
        return count



        