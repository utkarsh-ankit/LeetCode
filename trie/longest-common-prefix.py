class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        f=strs[0]
        while i<(len(strs)-1):
            t=[]
            j=0
            k=strs[i]
            p=strs[i+1]
            while j<len(k) and j<len(p):
                if k[j]==p[j]:
                    t.append(k[j])
                else:
                    break
                j+=1
            if not t:
                return ""
            f = ''.join(t)
            strs[i+1]=f
            i+=1
        return f

        