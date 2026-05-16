class Solution:
    def kMirror(self, k: int, n: int) -> int:
        def is_palindrome(s):
            return s == s[::-1]

        def to_base_k(x, k):
            res = []
            while x > 0:
                res.append(str(x % k))
                x //= k
            return ''.join(res[::-1])

        def generate_palindromes():
            length = 1
            while True:
                # Odd-length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[-2::-1])  # mirror except last digit
                # Even-length palindromes
                for half in range(10**(length - 1), 10**length):
                    s = str(half)
                    yield int(s + s[::-1])  # full mirror
                length += 1

        gen = generate_palindromes()
        total = 0
        count = 0

        while count < n:
            x = next(gen)
            if is_palindrome(to_base_k(x, k)):
                total += x
                count += 1

        return total
