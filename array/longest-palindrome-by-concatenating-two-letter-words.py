from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = Counter(words)
        res = 0
        has_center = False

        for w, c in count.items():
            rev = w[::-1]
            if w == rev:
                # pairs of the same word
                pairs = c // 2
                res += pairs * 4
                if c % 2:
                    has_center = True
            elif w < rev:
                # match with its reverse only once
                res += min(c, count.get(rev, 0)) * 4

        # if we can place one odd palindrome pair in the middle
        if has_center:
            res += 2

        return res
