class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count(prefix: int, next_prefix: int) -> int:
            cnt = 0
            while prefix <= n:
                cnt += min(n + 1, next_prefix) - prefix
                prefix *= 10
                next_prefix *= 10
            return cnt

        curr = 1
        k -= 1
        while k > 0:
            cnt = count(curr, curr + 1)
            if cnt <= k:
                curr += 1
                k -= cnt
            else:
                curr *= 10
                k -= 1
        return curr

        