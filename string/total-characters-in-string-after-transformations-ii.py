from typing import List

MOD = 1_000_000_007
ALPHA = 26          # number of lower-case letters

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        """
        onesᵀ · Aᵗ · c₀
        ---------------------------------
        • A  : 26×26 matrix, A[i][j] = 1  ⇢  letter j produces letter i
                                   = 0  otherwise
        • c₀ : column-vector of initial letter counts in s
        • onesᵀ : row-vector of all 1s (so the dot product sums all letters)
        """
        # ---------- build the 26×26 transition matrix --------------
        A = [[0]*ALPHA for _ in range(ALPHA)]
        for j in range(ALPHA):                      # “source” letter
            k = nums[j]
            for off in range(1, k+1):
                i = (j + off) % ALPHA              # “target” letter
                A[i][j] = 1                        # j → i happens once

        # ---------- fast-power: onesᵀ · Aᵗ -------------------------
        def row_mul(u, M):                          # u (1×26) · M (26×26)
            res = [0]*ALPHA
            for col in range(ALPHA):
                s = 0
                for k in range(ALPHA):
                    if u[k]:
                        s += u[k]*M[k][col]
                res[col] = s % MOD
            return res

        def mat_mul(X, Y):                          # X,Y ∈ ℤ/(MOD) 26×26
            Z = [[0]*ALPHA for _ in range(ALPHA)]
            for i in range(ALPHA):
                for k in range(ALPHA):
                    if X[i][k]:
                        xik = X[i][k]
                        for j in range(ALPHA):
                            Z[i][j] = (Z[i][j] + xik*Y[k][j]) % MOD
            return Z

        row = [1]*ALPHA                             # onesᵀ
        power = t
        base  = A
        while power:
            if power & 1:
                row = row_mul(row, base)            # multiply when bit is 1
            base = mat_mul(base, base)              # square the matrix
            power >>= 1

        # ---------- initial letter-count vector --------------------
        cnt = [0]*ALPHA
        for ch in s:
            cnt[ord(ch)-97] += 1

        # ---------- dot product → final length ---------------------
        ans = sum((row[i] * cnt[i]) % MOD for i in range(ALPHA)) % MOD
        return ans
