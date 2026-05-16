class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a=[]
        for i in tokens:
            if i not in {"+", "-", "*", "/"}:
                a.append(int(i))
            else:
                if i =="*":
                    a.append(a.pop(-2)*a.pop(-1))
                if i =="+":
                    a.append(a.pop(-2)+a.pop(-1))
                if i =="-":
                    a.append(a.pop(-2)-a.pop(-1))
                if i =="/":
                    a.append(int(a.pop(-2)/a.pop(-1)))                #need to do the int
        return a.pop()

