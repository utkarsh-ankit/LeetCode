class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l=0
        count=0
        char_count={'a':0, 'b':0, 'c':0}

        for r in range(len(s)):
            char_count[s[r]]+=1
            
            while char_count['a']>0 and char_count['b']>0 and char_count['c']>0:
                count+=len(s)-r

                char_count[s[l]]-=1
                l+=1
        return count






#First take 3 size sliding window, check that, then expand the window adn check and improve count, when reach to the end, go back to the initial sliding window, shift it by one and repeat the same steps
#Other smart idea, instead of looping all the way to the end if we found one abc, we can count the numbers(length of strings after r) after abc and add it to the count, it will help us to reduce time complexity



        