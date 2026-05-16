class Solution:
    def kthCharacter(self, k: int) -> str:
        def helper(length, k):
            if length == 1:
                return 'a'
            prev_len = length // 2
            if k <= prev_len:
                return helper(prev_len, k)
            else:
                c = helper(prev_len, k - prev_len)
                return chr((ord(c) - ord('a') + 1) % 26 + ord('a'))
        
        length = 1
        while length < k:
            length *= 2
        return helper(length, k)
