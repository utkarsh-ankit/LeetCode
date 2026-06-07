class Solution:
    def getMoneyAmount(self, n: int) -> int:

        def play(l,h):
            if l>=h:
                return 0

            best=float('inf')

            for guess in range(l,h+1):
                worst=guess+max(play(l,guess-1), play(guess+1,h))

                best=min(best, worst)

            return best

        return play(1,n)


        