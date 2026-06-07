class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2=len(s1), len(s2)

        if len_s1>len_s2:
            return False

        count_s1=Counter(s1)
        s_window=Counter(s2[:len_s1])


        if count_s1==s_window:
            return True

        for i in range(len_s1, len_s2):
            s_window[s2[i]]+=1
            l=s2[i-len_s1]
            s_window[l]-=1

            if count_s1==s_window:
                return True
        return False
        
# from collections import Counter

# class Solution:
#     def checkInclusion(self, s1: str, s2: str) -> bool:
#         len_s1, len_s2 = len(s1), len(s2)
        
#         if len_s1 > len_s2:
#             return False
            
#         # Create a frequency map for s1 and the first window of s2
#         count_s1 = Counter(s1)
#         window_count = Counter(s2[:len_s1])
        
#         # Check the first window
#         if count_s1 == window_count:
#             return True
            
#         # Slide the window
#         for i in range(len_s1, len_s2):
#             # Add the new character entering the window
#             window_count[s2[i]] += 1
            
#             # Identify and subtract the character leaving the window
#             left_char = s2[i - len_s1]
#             window_count[left_char] -= 1
            
#             # Crucial step: remove the key if its count drops to 0 
#             # so the dictionary comparison works perfectly
#             if window_count[left_char] == 0:
#                 del window_count[left_char]
                
#             # Compare the dictionaries
#             if count_s1 == window_count:
#                 return True
                
#         return False