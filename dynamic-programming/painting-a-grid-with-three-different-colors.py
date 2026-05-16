class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        MOD = 10**9 + 7
        
        # 1. Generate all valid masks for a column of height m
        valid_masks = []
        def is_valid(mask):
            prev_color = -1
            for _ in range(m):
                color = mask % 3
                if color == prev_color:
                    return False
                prev_color = color
                mask //= 3
            return True
        
        for mask in range(3**m):
            if is_valid(mask):
                valid_masks.append(mask)
        
        K = len(valid_masks)
        
        # 2. Precompute compatibility: transitions[i] = list of j where valid_masks[i] & valid_masks[j] compatible
        transitions = [[] for _ in range(K)]
        for i, a in enumerate(valid_masks):
            for j, b in enumerate(valid_masks):
                ok = True
                x, y = a, b
                for _ in range(m):
                    if x % 3 == y % 3:  # same color in same row
                        ok = False
                        break
                    x //= 3
                    y //= 3
                if ok:
                    transitions[i].append(j)
        
        # 3. DP across columns using rolling arrays
        dp = [1] * K  # dp for column 0
        for _ in range(1, n):
            new_dp = [0] * K
            for i in range(K):
                for j in transitions[i]:
                    new_dp[i] = (new_dp[i] + dp[j]) % MOD
            dp = new_dp
        
        # 4. Sum over ways to end in any mask at last column
        return sum(dp) % MOD
