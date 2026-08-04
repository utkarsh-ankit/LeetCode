class Solution:
    def maxLength(self, arr: List[str]) -> int:
        c_set=set()

        def overlap(c_set,s):
            prev=set()
            for c in s:
                if c in c_set or c in prev:
                    return True
                prev.add(c)  #check if same letter is repeated in one string
            return False
        
        def backtrack(i):
            if i==len(arr):
                return len(c_set)

            res=0
            if not overlap(c_set,arr[i]):
                for c in arr[i]:
                    c_set.add(c)
                res=backtrack(i+1)
                for c in arr[i]:
                    c_set.remove(c)

            return max(res,backtrack(i+1))

        return backtrack(0)