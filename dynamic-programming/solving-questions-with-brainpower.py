from typing import List

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo={}

        def rec(i):
            if i>=len(questions):
                return 0
            if i in memo:
                return memo[i]

            value, jump=questions[i]
            solve=value+rec(i+jump+1)
            skip=rec(i+1)

            memo[i]=max(solve,skip)
            return memo[i]

        return rec(0)

