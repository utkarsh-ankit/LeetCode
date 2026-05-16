class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        cnt_even = cnt_odd = even_alt = odd_alt = 0
        
        for x in nums:
            parity = x & 1
            if parity == 0:
                cnt_even += 1
                even_alt = max(even_alt, odd_alt + 1)
            else:
                cnt_odd += 1
                odd_alt = max(odd_alt, even_alt + 1)
        
        # longest same-parity must have at least two elements
        same_parity_max = max(cnt_even, cnt_odd)
        # alternating must have length ≥ 2, but our logic auto ensures that

        return max(same_parity_max, even_alt, odd_alt)
