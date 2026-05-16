class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        ope=["(","[","{"]
        clo=[")","]","}"]
        if len(s)%2!=0:
            return False
        for i in range(len(s)):
            if s[i] in ope and (not stack or stack[-1] in ope):
                stack.append(s[i])
            elif s[i] in clo and stack:
                if s[i]==")" and (stack[-1]=="("):
                    stack.pop()
                elif s[i]=="]" and (stack[-1]=="["):
                    stack.pop()
                elif s[i]=="}" and (stack[-1]=="{"):
                    stack.pop()
                else:
                    return False
            else:
                return False
        return True if not stack else False

        

        