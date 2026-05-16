class Solution:
    def minMaxDifference(self, num: int) -> int:
        b=[]
        c=[]
        a=str(num)
        z=0
        k=0

        for i in a:
            b.append(int(i))
            c.append(int(i))

        for i in range(len(b)):
            if b[i]!=9:
                z=b[i]
                break

        for i in range(len(b)):
            if b[i]==z:
                b[i]=9
            l="".join([str(p) for p in b])

        for i in range(len(c)):
            if c[i]!=0:
                k=c[i]
                break

        for i in range(len(c)):
            if c[i]==k:
                c[i]=0
        o="".join([str(p) for p in c])
        return (int(l)-int(o))
        