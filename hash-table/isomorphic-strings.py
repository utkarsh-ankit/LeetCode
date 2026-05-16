class Solution:
    def st(self, k:str)-> list:

        char_t_num={}

        f=[]

        counter = 1

        for i in k:
            if i not in char_t_num:
                char_t_num[i]=counter
                counter+=1
            f.append(char_t_num[i])

        return f

    def isIsomorphic(self, s: str, t: str) -> bool:
        s=self.st(s)
        t=self.st(t)
        return s==t

        