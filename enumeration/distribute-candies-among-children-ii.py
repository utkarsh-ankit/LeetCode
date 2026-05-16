class Solution:
    def combinations(self, n: int) -> int:
        if n < 0:
            return 0
        return (n + 1) * (n + 2) // 2

    def distributeCandies(self, n: int, limit: int) -> int:
        all_combinations = self.combinations(n)
        one_above_limit_combinations = 3 * self.combinations(n - (limit + 1))
        two_above_limit_combinations = 3 * self.combinations(n - 2 * (limit + 1))
        three_above_limit_combinations = self.combinations(n - 3 * (limit + 1))

        invalid_combinations = (one_above_limit_combinations - 
                               two_above_limit_combinations + 
                               three_above_limit_combinations)
        valid_combinations = all_combinations - invalid_combinations
        return valid_combinations