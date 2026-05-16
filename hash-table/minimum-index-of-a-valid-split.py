class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # def half(a):
        #     if not a:
        #         return -1
        #     count=Counter(a)
        #     element, frequency=count.most_common(1)[0]
        #     if frequency>len(a)//2:
        #         return element
        #     else:
        #         return -1

        # t=half(nums)
        # if t!=-1:
        #     for i in range(len(nums)):
        #         if nums[i]==t:
        #             if half(nums[:i])==t and half(nums[i:])==t:
        #                 return i-1
        #                 break
        #             else:
        #                 continue
        #     return -1



        # def half(a):
        #     if not a:
        #         return -1
        #     count=Counter(a)
        #     element, frequency = count.most_common(1)[0]
        #     if frequency > len(a)//2:
        #         return element
        #     else:
        #         return -1

        # t = half(nums)
        # if t != -1:
        #     for i in range(1, len(nums)):
        #         if half(nums[:i]) == t and half(nums[i:]) == t:
        #             return i-1
        #     return -1
        # else:
        #     return -1



        # 1) Find the dominant element t
        count = Counter(nums)
        t, freq = count.most_common(1)[0]
        n = len(nums)
        if freq <= n // 2:
            return -1  # no valid dominant element

        # 2) Build prefix_count array
        prefix_count = [0] * (n + 1)  
        # prefix_count[i] = count of t in nums[:i]
        # e.g. prefix_count[0] = 0, prefix_count[1] = (nums[0] == t ? 1 : 0), etc.
        for i in range(n):
            prefix_count[i+1] = prefix_count[i] + (1 if nums[i] == t else 0)

        # 3) Check each possible split i
        for i in range(1, n):  # can't split at i=0 or i=n
            left_len = i
            right_len = n - i
            left_t = prefix_count[i]  # count of t in nums[:i]
            right_t = freq - left_t   # count of t in nums[i:]

            if left_t > left_len // 2 and right_t > right_len // 2:
                return i-1

        return -1



