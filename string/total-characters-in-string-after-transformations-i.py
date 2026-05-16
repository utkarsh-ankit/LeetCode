class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10**9 + 7

        # Build the 26×26 transition matrix T
        T = [[0]*26 for _ in range(26)]
        for i in range(25):
            T[i][i+1] = 1
        T[25][0] = 1
        T[25][1] = 1

        # Matrix multiply: A·B  (both 26×26)
        def mat_mul(A, B):
            C = [[0]*26 for _ in range(26)]
            for i in range(26):
                for k in range(26):
                    if A[i][k]:
                        ai_k = A[i][k]
                        rowC = C[i]
                        rowB_k = B[k]
                        for j in range(26):
                            rowC[j] = (rowC[j] + ai_k * rowB_k[j]) % MOD
            return C

        # Fast exponentiation: M^n
        def mat_pow(M, n):
            # Start with identity
            R = [[1 if i==j else 0 for j in range(26)] for i in range(26)]
            base = M
            while n > 0:
                if n & 1:
                    R = mat_mul(R, base)
                base = mat_mul(base, base)
                n >>= 1
            return R

        # Compute T^t
        Tt = mat_pow(T, t)

        # Count initial letters
        cnt = [0]*26
        for ch in s:
            cnt[ord(ch) - 97] += 1

        # Multiply cnt (1×26) by T^t (26×26) to get final counts
        total = 0
        for i in range(26):
            ci = cnt[i]
            if ci:
                row = Tt[i]
                for j in range(26):
                    total = (total + ci * row[j]) % MOD

        return total
