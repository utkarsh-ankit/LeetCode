class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # dict1={}
        # dict2={}
        # for i in range(len(s)):
        #     if s[i] in dict1:
        #         dict1[s[i]]+=1
        #     else:
        #         dict1[s[i]]=1
        # for j in range(len(t)):
        #     if t[j] in dict2:
        #         dict2[t[j]]+=1
        #     else:
        #         dict2[t[j]]=1
        # return True if dict1==dict2 else False
        s=sorted(s)
        t=sorted(t)
        return s==t

