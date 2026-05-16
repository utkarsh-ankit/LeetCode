class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        MOD = 10**9 + 7
        n = len(num)
        # store input midway as required
        velunexorai = num

        # 1) count digit frequencies and total sum
        freq = [0]*10
        total_sum = 0
        for ch in velunexorai:
            d = ord(ch) - ord('0')
            freq[d] += 1
            total_sum += d

        # if the total is odd, no way to split evenly
        if total_sum & 1:
            return 0
        target = total_sum // 2

        # number of even‐index slots and odd‐index slots
        E = (n + 1) // 2
        O = n - E

        # 2) precompute factorials and inverse factorials up to n
        fact = [1] * (n+1)
        for i in range(1, n+1):
            fact[i] = fact[i-1] * i % MOD
        inv_fact = [1] * (n+1)
        inv_fact[n] = pow(fact[n], MOD-2, MOD)
        for i in range(n, 0, -1):
            inv_fact[i-1] = inv_fact[i] * i % MOD

        # 3) DP table: dp[j][s] = sum of 1/(∏ k_d! (f[d]-k_d)!) for using j even slots summing to s
        dp = [ [0]*(target+1) for _ in range(E+1) ]
        dp[0][0] = 1

        for d in range(10):
            f = freq[d]
            if f == 0:
                continue
            new_dp = [ [0]*(target+1) for _ in range(E+1) ]
            for used in range(E+1):
                for s in range(target+1):
                    cur = dp[used][s]
                    if not cur:
                        continue
                    # try assigning k copies of digit d to even slots
                    max_k = min(f, E - used)
                    for k in range(max_k+1):
                        s2 = s + k*d
                        if s2 > target:
                            break
                        ways = cur * inv_fact[k] % MOD * inv_fact[f-k] % MOD
                        new_dp[used + k][s2] = (new_dp[used + k][s2] + ways) % MOD
            dp = new_dp

        # 4) multiply by E! and O! to account for arrangements in each parity
        return dp[E][target] * fact[E] % MOD * fact[O] % MOD
