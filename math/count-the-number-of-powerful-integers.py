class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        A = int(s)
        m = len(s)
        B = 10 ** m
        
        # Compute p_min and p_max so that candidate = p * B + A is in [start, finish]
        if start <= A:
            p_min = 0
        else:
            # ceiling division for positive numbers
            p_min = (start - A + B - 1) // B
        
        if finish < A:
            return 0  # No candidate can be valid if even A > finish.
        p_max = (finish - A) // B
        
        # Digit DP to count numbers in [0, X] whose digits are all in [0, limit].
        from functools import lru_cache
        def count_valid(X: int) -> int:
            if X < 0:
                return 0
            digits = list(map(int, str(X)))
            n = len(digits)
            
            @lru_cache(maxsize=None)
            def dp(i: int, tight: bool, leading: bool) -> int:
                if i == n:
                    # At the end, we have constructed one valid number (even if it is 0).
                    return 1
                total = 0
                # upper bound for the current digit
                ub = digits[i] if tight else limit
                # However, if tight and digits[i] > limit, then the allowed maximum is still limit,
                # because we are not allowed to choose a digit greater than limit.
                ub = min(ub, limit)
                for d in range(0, ub + 1):
                    # if we are still in the leading zeros phase, we can choose 0.
                    new_leading = leading and (d == 0)
                    new_tight = tight and (d == digits[i])
                    total += dp(i + 1, new_tight, new_leading)
                return total
            
            return dp(0, True, True)
        
        # Count valid prefix numbers p in [p_min, p_max]
        total_valid = count_valid(p_max) - count_valid(p_min - 1)
        return total_valid