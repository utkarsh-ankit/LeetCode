class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        MOD = 10**9 + 7

        # 1) Build groups of consecutive characters
        groups = []
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            groups.append(j - i)
            i = j

        # 2) Total combinations: product of group sizes
        total = 1
        for g in groups:
            total = total * g % MOD

        # If enough groups already
        if len(groups) >= k:
            return total

        # 3) Count invalid (length < k) using DP
        dp = [0] * k
        dp[0] = 1  # empty selection

        for idx, g in enumerate(groups):
            new_dp = [0] * k
            window = 0
            for j in range(idx, k):
                # window = sum(dp[j - g .. j - 1])
                new_dp[j] = window
                window = (window + dp[j]) % MOD
                if j - g >= 0:
                    window = (window - dp[j - g] + MOD) % MOD
            dp = new_dp

        invalid = sum(dp) % MOD
        return (total - invalid + MOD) % MOD
