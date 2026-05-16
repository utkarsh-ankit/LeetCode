class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        num=0
        sign="+"

        for i in range(len(s)):
            ch=s[i]

            if ch.isdigit():
                num=(num*10 + int(ch))

            if (ch in "+-*/") or (i==(len(s)-1)):
                if sign=="+":
                    stack.append(num)
                elif sign=="-":
                    stack.append(-1*num)
                elif sign=="*":
                    stack[-1]=stack[-1]*num
                elif sign=="/":
                    stack[-1]=int(stack[-1]/num)

                sign=ch
                num=0

        return sum(stack)

        