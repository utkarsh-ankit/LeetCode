class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        from collections import Counter

        max_dist = 0
        x = y = 0
        cnt = Counter()

        for move in s:
            cnt[move] += 1

            if move == 'N':
                y += 1
            elif move == 'S':
                y -= 1
            elif move == 'E':
                x += 1
            elif move == 'W':
                x -= 1

            cur_dist = abs(x) + abs(y)

            # Opposite directions canceling each other
            cancel_x = min(cnt['W'], cnt['E'])
            cancel_y = min(cnt['N'], cnt['S'])
            total_cancel = cancel_x + cancel_y

            fix = min(k, total_cancel)

            improved_dist = cur_dist + 2 * fix
            max_dist = max(max_dist, improved_dist)

        return max_dist

        