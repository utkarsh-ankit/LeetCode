class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def strin(p):
            stack=[]
            for i in p:
                if i!='#':
                    stack.append(i)
                elif i=='#' and stack:
                    stack.pop()
                else:
                    continue
            return stack
        return strin(s)==strin(t)

        # def sringofi(k):
        #     for i in range(1, len(k)):
        #         if k[i]=='#':
        #             k.pop(i-1)
        #             k.pop(i)
        #         return k
        # return sringofi(s)==sringofi(t)

        


        