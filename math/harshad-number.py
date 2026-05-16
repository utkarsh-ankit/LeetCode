class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        p=0
        a=list(str(x))
        for i in a:
            p+=int(i)
        if x%p==0:
            return p
        return -1