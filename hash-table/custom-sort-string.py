class Solution:
    def customSortString(self, order: str, s: str) -> str:
        a={char:s.count(char) for char in s}
        p=''

        for i in order:
            while a.get(i,0)>0:
                p+=i
                a[i]-=1
        
        for char, coun in a.items():
            p+=char*coun
        
        return p

        