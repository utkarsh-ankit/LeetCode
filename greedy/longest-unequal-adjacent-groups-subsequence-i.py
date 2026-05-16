
from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        last = -1
        for w, g in zip(words, groups):
            if g != last:
                result.append(w)
                last = g
        return result
