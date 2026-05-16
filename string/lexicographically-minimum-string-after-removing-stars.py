class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        # letter_positions[i] holds a stack of indices where chr(ord('a')+i) appears
        letter_positions = [[] for _ in range(26)]
        removed = [False] * n

        # 1) Sweep left to right, handling letters vs. stars
        for i, ch in enumerate(s):
            if ch == '*':
                # mark the star removed
                removed[i] = True
                # find the smallest letter with a nonempty stack
                for li in range(26):
                    if letter_positions[li]:
                        pos = letter_positions[li].pop()
                        removed[pos] = True
                        break
            else:
                # record this letter’s position
                letter_positions[ord(ch) - ord('a')].append(i)

        # 2) Build the answer by skipping removed positions and any stars
        return "".join(
            s[i] for i in range(n)
            if not removed[i] and s[i] != '*'
        )
