class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends==1:
            return word

        n = len(word)
        # Each of the other (numFriends - 1) pieces must use ≥1 char,
        # so any single piece can be at most (n - (numFriends - 1)) long.
        maxLen = n - (numFriends - 1)

        # 1) Find the starting index `best` of the lexicographically largest suffix in O(n):
        i, j, k = 0, 1, 0
        # i = candidate for “best so far”
        # j = yet‐to‐compare suffix start
        # k = how many characters we have matched so far
        while j + k < n:
            if word[i + k] == word[j + k]:
                k += 1
                continue
            if word[i + k] > word[j + k]:
                # suffix at i is still ≥ suffix at j, so skip over j
                j = j + k + 1
            else:
                # suffix at j is larger, so jump i forward
                new_i = j
                # ensure we never “rewind” j below i
                j = max(i + k + 1, j + 1)
                i = new_i
            k = 0

        # 2) Now i is the start of the lexicographically largest suffix.
        #    Return up to maxLen characters from word[i:].
        return word[i : i + maxLen]

