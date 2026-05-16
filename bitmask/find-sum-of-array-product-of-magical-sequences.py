from typing import List

class Solution:
    def magicalSum(self, M: int, K: int, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        fact = [1] * (M+1)
        for i in range(1, M+1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1] * (M+1)
        inv_fact[M] = pow(fact[M], MOD-2, MOD)
        for i in range(M, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD


        W = [[1]*(M+1) for _ in range(n)]
        for i in range(n):
            for t in range(1, M+1):
                W[i][t] = pow(nums[i], t, MOD) * inv_fact[t] % MOD

        dp = [[[0]*(M+1) for _ in range(K+1)] for __ in range(M+1)]
        dp[0][0][0] = 1

        for i in range(n):
            dp2 = [[[0]*(M+1) for _ in range(K+1)] for __ in range(M+1)]
            for c in range(M+1):
                for ones in range(K+1):
                    for used in range(M+1):
                        v = dp[c][ones][used]
                        if not v:
                            continue

                        for t in range(M - used + 1):
                            nc  = (c + t) >> 1
                            bit = (c + t) & 1
                            no  = ones + bit
                            if no > K:
                                continue      
                            nu = used + t
                            dp2[nc][no][nu] = (dp2[nc][no][nu] 
                                               + v * W[i][t]) % MOD
            dp = dp2

        ans = 0
        for c in range(M+1):
            extra = bin(c).count("1")
            for ones in range(K+1):
                if ones + extra == K:
                    ans = (ans + dp[c][ones][M]) % MOD

        return ans * fact[M] % MOD
