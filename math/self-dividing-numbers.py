class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            a=str(i)
            for j in a:
                if j=="0" or i%int(j)!=0:
                    break
            else:
                res.append(int(a))
        return res
        