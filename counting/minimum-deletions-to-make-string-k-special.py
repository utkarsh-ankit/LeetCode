from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = Counter(word)
        freq_values = sorted(freq.values())
        n = len(freq_values)
        prefix_sum = [0] * (n + 1)
        
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + freq_values[i]
        
        res = float('inf')
        for i in range(n):
            # freq_values[i] is the min frequency we try to keep
            min_freq = freq_values[i]
            max_allowed = min_freq + k
            
            # Delete all chars with freq < min_freq (prefix sum)
            deletions = prefix_sum[i]
            
            # Delete all chars with freq > max_allowed
            j = i
            while j < n and freq_values[j] <= max_allowed:
                j += 1
            for x in range(j, n):
                deletions += freq_values[x] - max_allowed
            
            res = min(res, deletions)
        
        return res
