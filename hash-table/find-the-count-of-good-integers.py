from collections import Counter
from math import factorial

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def generate_all_palindromes(n):
            palindromes = []
            half_len = (n + 1) // 2
            start = 10**(half_len - 1)
            end = 10**half_len

            for first_half in range(start, end):
                half_str = str(first_half)
                if n % 2 == 0:
                    full = half_str + half_str[::-1]
                else:
                    full = half_str + half_str[:-1][::-1]
                palindromes.append(full)
            return palindromes

        def count_permutations_without_leading_zero(digits):
            counter = Counter(digits)
            total = 0
            for first_digit in set(digits):
                if first_digit == '0':
                    continue
                counter[first_digit] -= 1
                perms = factorial(len(digits) - 1)
                for v in counter.values():
                    perms //= factorial(v)
                total += perms
                counter[first_digit] += 1
            return total

        palindromes = generate_all_palindromes(n)
        seen_digit_multisets = set()
        total_good = 0

        for p in palindromes:
            if int(p) % k == 0:
                digits = list(p)
                digit_tuple = tuple(sorted(digits))
                if digit_tuple in seen_digit_multisets:
                    continue
                seen_digit_multisets.add(digit_tuple)
                total_good += count_permutations_without_leading_zero(digits)

        return total_good
