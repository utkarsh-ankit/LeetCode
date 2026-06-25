class Solution:
    def isValid(self, s: str) -> bool:
        a={"}":"{", "]":"[", ")":"("}
        stack=[]

        for i in s:
            if i in ("{", "(", "["):
                stack.append(i)
            elif i in a and stack and a[i]==stack[-1]:
                stack.pop()
            else:
                return False
        return True if not stack else False


        