from collections import Counter

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:
        MOD = 10**9 + 7

        # Sieve to get smallest prime factors (SPF) for fast factorization
        spf = list(range(maxValue + 1))
        for i in range(2, int(maxValue**0.5) + 1):
            if spf[i] == i:
                for j in range(i * i, maxValue + 1, i):
                    if spf[j] == j:
                        spf[j] = i

        def get_factors(x):
            count = Counter()
            while x > 1:
                count[spf[x]] += 1
                x //= spf[x]
            return count

        # Precompute factorials and inverse factorials
        MAX = n + 14
        factorial = [1] * MAX
        inv_factorial = [1] * MAX

        for i in range(1, MAX):
            factorial[i] = factorial[i - 1] * i % MOD

        inv_factorial[MAX - 1] = pow(factorial[MAX - 1], MOD - 2, MOD)
        for i in range(MAX - 2, -1, -1):
            inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD

        def comb(a, b):
            if b < 0 or b > a:
                return 0
            return factorial[a] * inv_factorial[b] % MOD * inv_factorial[a - b] % MOD

        # Main computation
        result = 0
        for x in range(1, maxValue + 1):
            pf = get_factors(x)
            ways = 1
            for exp in pf.values():
                ways = ways * comb(n + exp - 1, exp) % MOD
            result = (result + ways) % MOD

        return result
