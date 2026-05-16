class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        
        # Build the maximum a by replacing the first non‐'9' digit with '9'
        x_a = None
        for ch in s:
            if ch != '9':
                x_a = ch
                break
        if x_a is not None:
            a = int(s.replace(x_a, '9'))
        else:
            a = num

        # Build the minimum b
        # If the first digit is not '1', replace all occurrences of it with '1'
        if s[0] != '1':
            x_b = s[0]
            b = int(s.replace(x_b, '1'))
        else:
            # Otherwise, replace the first digit after index 0 that is neither '0' nor '1' with '0'
            x_b = None
            for ch in s[1:]:
                if ch not in ('0', '1'):
                    x_b = ch
                    break
            if x_b is not None:
                b = int(s.replace(x_b, '0'))
            else:
                b = num

        return a - b

        