class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset=set()
        left=0
        length=0

        for i in range(len(s)):           #slidingwindow and set
            while s[i] in charset:
                charset.remove(s[left])
                left+=1
            
            charset.add(s[i])
            length=max(length, i-left+1)

        return length









        