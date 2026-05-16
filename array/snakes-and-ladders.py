from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        if n == 1:
            return 0

        # Build a list 'flat' where flat[i] = destination square or -1
        flat = [0] * (n * n + 1)
        idx = 1
        left_to_right = True
        for row in range(n - 1, -1, -1):
            if left_to_right:
                for col in range(n):
                    flat[idx] = board[row][col]
                    idx += 1
            else:
                for col in range(n - 1, -1, -1):
                    flat[idx] = board[row][col]
                    idx += 1
            left_to_right = not left_to_right

        dist = [-1] * (n * n + 1)
        q = deque([1])
        dist[1] = 0

        while q:
            curr = q.popleft()
            for step in range(1, 7):
                nxt = curr + step
                if nxt > n * n:
                    break
                dest = flat[nxt]
                final = dest if dest != -1 else nxt
                if dist[final] == -1:
                    dist[final] = dist[curr] + 1
                    if final == n * n:
                        return dist[final]
                    q.append(final)

        return -1
