class Solution:
    def countLargestGroup(self, n: int) -> int:
        # def digit_sum(x):
        #     return sum(int(digit) for digit in str(n))
        def digit_sum(x):
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s

        a={i:[] for i in range(1,37)}
        for i in range(1,n+1):
            t = digit_sum(i)
            a[t].append(i)
        
        p = max(a, key=lambda x: len(a[x]))
        max_len = len(a[p])
        count=0

        for value in a.values():
            if len(value) == max_len:
                count += 1
        return count




        

            
        