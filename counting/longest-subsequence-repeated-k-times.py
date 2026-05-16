from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        def is_subsequence(t):
            j = 0
            for ch in s:
                if t[j] == ch:
                    j += 1
                    if j == len(t):
                        return True
            return False
        
        def is_valid(seq):
            # Check if seq * k is a subsequence of s
            t = seq * k
            return is_subsequence(t)
        
        # Step 1: Only use characters that appear at least k times
        count = Counter(s)
        valid_chars = [ch for ch in count if count[ch] >= k]
        valid_chars.sort(reverse=True)  # Lexicographically largest first

        max_len = len(s) // k
        q = deque([''])
        best = ''

        while q:
            cur = q.popleft()
            for ch in valid_chars:
                new_seq = cur + ch
                if len(new_seq) > max_len:
                    continue
                if is_valid(new_seq):
                    if len(new_seq) > len(best) or (len(new_seq) == len(best) and new_seq > best):
                        best = new_seq
                    q.append(new_seq)

        return best

        