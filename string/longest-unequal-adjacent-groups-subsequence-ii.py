from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        # Precompute lengths for quick checks
        lengths = [len(w) for w in words]

        # Hamming-distance == 1 checker in O(L) time
        def is_hamming_one(a: str, b: str) -> bool:
            diff = 0
            for x, y in zip(a, b):
                if x != y:
                    diff += 1
                    if diff > 1:
                        return False
            return diff == 1  # exactly one difference :contentReference[oaicite:0]{index=0}

        # DP arrays: dp[i] = length of longest valid subsequence ending at i
        dp = [1] * n
        parent = [-1] * n

        # Build the DAG and compute DP in topological order 0..n-1 :contentReference[oaicite:1]{index=1}
        for i in range(n):
            for j in range(i+1, n):
                if (groups[i] != groups[j] and
                    lengths[i] == lengths[j] and
                    is_hamming_one(words[i], words[j])):
                    # Relax edge i→j
                    if dp[i] + 1 > dp[j]:
                        dp[j] = dp[i] + 1
                        parent[j] = i

        # Find the maximum dp value
        max_len = max(dp)  # at least 1 since each word alone is valid :contentReference[oaicite:2]{index=2}

        # Tie-break by choosing the largest index with dp == max_len
        end = max(idx for idx, val in enumerate(dp) if val == max_len)

        # Reconstruct the path (in reverse) and then map to words :contentReference[oaicite:3]{index=3}
        seq = []
        while end != -1:
            seq.append(words[end])
            end = parent[end]
        seq.reverse()
        return seq
