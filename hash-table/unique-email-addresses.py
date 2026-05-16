class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        l=[]
        for i in range(len(emails)):
            v=emails[i].find('@')
            q=emails[i][:v].replace('.','')
            k=emails[i][v:]

            o=q.find('+')
            if o!=-1:
                q=q[:o]

            z= q+k
            l.append(z)
        return len(set(l))



        