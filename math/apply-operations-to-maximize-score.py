from typing import List

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Step 1: Build SPF (Smallest Prime Factor)
        def build_spf(max_val):
            spf = [0] * (max_val + 1)
            for i in range(2, max_val + 1):
                if spf[i] == 0:
                    for j in range(i, max_val + 1, i):
                        if spf[j] == 0:
                            spf[j] = i
            return spf

        # Step 2: Get Prime Score using SPF
        def get_prime_score(x, spf):
            factors = set()
            while x > 1:
                factors.add(spf[x])
                x //= spf[x]
            return len(factors)

        max_val = max(nums)
        spf = build_spf(max_val)

        # Prime score for each number
        prime_scores = [get_prime_score(x, spf) for x in nums]

        # Step 3: Monotonic stack to count subarrays where nums[i] is dominant
        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            while stack and prime_scores[stack[-1]] < prime_scores[i]:
                stack.pop()
            left[i] = i - stack[-1] if stack else i + 1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and prime_scores[stack[-1]] <= prime_scores[i]:
                stack.pop()
            right[i] = stack[-1] - i if stack else n - i
            stack.append(i)

        # Step 4: Collect candidates as (value, usable_times)
        elements = []
        for i in range(n):
            count = left[i] * right[i]
            elements.append((nums[i], count))

        # Step 5: Sort by value descending
        elements.sort(reverse=True)

        # Step 6: Apply top k multiplications
        score = 1
        for val, freq in elements:
            use = min(freq, k)
            score = (score * pow(val, use, MOD)) % MOD
            k -= use
            if k == 0:
                break

        return score
