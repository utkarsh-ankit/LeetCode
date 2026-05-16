# class Solution:
#     def countGoodNumbers(self, n: int) -> int:
#         count=0
#         a=set()
#         t=[2,3,5,7]
#         for i in range(10,100):
#             i=str(i)
#             if int(i[0])%2==0 and int(i[1]) in t:
#                 a.add(int(i))

#         if n==1:
#             return 5
#         elif n==2:
#             return 16
#         elif n%2==0:
#             for i in range(10**(n-1), (10**n)):
#                 i=str(i)
#                 t=0
#                 while t < len(i) - 1: 
#                     if int(i[t]+i[t+1]) not in a:
#                         break
#                     t+=2
#                 else:
#                     count+=1
#         else:
#             for i in range(10**(n-1), (10**n)):
#                 i=str(i)
#                 if int(i[-1])%2!=0:
#                     continue
#                 t=0
#                 while t < len(i) - 1:
#                     if int(i[t]+i[t+1]) not in a:
#                         break
#                     t+=2
#                 else:
#                     count+=1

#         return count

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7
        even = (n + 1) // 2  # positions: 0, 2, 4, ...
        odd = n // 2         # positions: 1, 3, 5, ...
        
        return (pow(5, even, mod) * pow(4, odd, mod)) % mod


                




        

        