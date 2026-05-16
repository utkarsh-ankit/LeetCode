class Solution:
    def maxProduct(self, n: int) -> int:
        a=str(n)
        b= "".join(sorted(a))
        return int(b[-1])*int(b[-2])
        