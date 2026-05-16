class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # diff array of size length+1, initialized to 0
        diff = [0] * (length + 1)

        # apply each update [start, end, inc]
        # we add inc at diff[start], and subtract inc at diff[end+1]
        for start, end, inc in updates:
            diff[start] += inc
            diff[end + 1] -= inc

        # build the result by prefix‐summing diff (ignore the extra slot at the end)
        res = [0] * length
        running = 0
        for i in range(length):
            running += diff[i]
            res[i] = running

        return res
