from functools import lru_cache

class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> list[int]:
        @lru_cache(None)
        def dp(l: int, r: int, k: int) -> tuple[int, int]:
            # l: rank (from front) of player1
            # r: rank (from back) of player2
            # k: current total number of players
            if l == r:
                # They meet in this round
                return (1, 1)
            if l > r:
                return dp(r, l, k)
            
            earliest = float('inf')
            latest = 0
            half = (k + 1) // 2
            
            # Try all possible positions of l and r in next round
            for i in range(1, l + 1):
                for j in range(l - i + 1, r - i + 1):
                    total = i + j
                    if not (l + r - k // 2 <= total <= half):
                        continue
                    sub_e, sub_l = dp(i, j, half)
                    earliest = min(earliest, sub_e + 1)
                    latest = max(latest, sub_l + 1)
            
            return (earliest, latest)

        # Convert secondPlayer to 'r' from the back
        return list(dp(firstPlayer, n - secondPlayer + 1, n))
