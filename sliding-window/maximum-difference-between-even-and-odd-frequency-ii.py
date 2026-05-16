from collections import deque
from typing import Deque

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        # map characters '0'–'4' to integers 0–4
        arr = [ord(ch) - ord('0') for ch in s]

        INF = float('inf')
        NEG_INF = float('-inf')
        answer = NEG_INF

        # try every ordered pair (a, b), a != b
        for a_digit in range(5):
            for b_digit in range(5):
                if a_digit == b_digit:
                    continue

                # prefix counts and parities
                A = [0] * (n + 1)
                B = [0] * (n + 1)
                P_a = [0] * (n + 1)
                P_b = [0] * (n + 1)
                C = [0] * (n + 1)  # C[j] = A[j] - B[j]

                for i in range(1, n + 1):
                    A[i] = A[i-1] + (arr[i-1] == a_digit)
                    B[i] = B[i-1] + (arr[i-1] == b_digit)
                    P_a[i] = A[i] & 1
                    P_b[i] = B[i] & 1
                    C[i]   = A[i] - B[i]

                # For each of the 4 parity states, track min C[i]
                min_C_state = [INF] * 4
                # Queues of (B_i, C_i) waiting until B[j] - B[i] >= 2
                waiting: list[Deque[tuple[int,int]]] = [deque() for _ in range(4)]
                best_for_pair = NEG_INF

                for j in range(1, n + 1):
                    i = j - k
                    if i >= 0:
                        st_i = (P_a[i] << 1) | P_b[i]
                        waiting[st_i].append((B[i], C[i]))

                    # need B[i] <= B[j] - 2
                    threshold = B[j] - 2

                    for st in range(4):
                        dq = waiting[st]
                        while dq and dq[0][0] <= threshold:
                            b_i, c_i = dq.popleft()
                            if c_i < min_C_state[st]:
                                min_C_state[st] = c_i

                    st_j = (P_a[j] << 1) | P_b[j]
                    needed = (((1 - P_a[j]) << 1) | P_b[j])
                    min_c = min_C_state[needed]
                    if min_c != INF:
                        diff = C[j] - min_c
                        if diff > best_for_pair:
                            best_for_pair = diff

                if best_for_pair > answer:
                    answer = best_for_pair

        return answer
