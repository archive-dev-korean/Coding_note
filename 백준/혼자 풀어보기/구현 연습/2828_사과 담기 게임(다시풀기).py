# #구현 연습
# N,M=map(int,input().split())
# J=int(input())
# s=[]
# for _ in range(J):
#     i=int(input())
#     s.append(i)
# if M ==1:
#     ans=0
#     for j in range(1,len(s)):
#         ans+=abs(s[j]-s[j-1])
# else:
#     for k in s:
#         if k>M:
#             for j in range(1,len(s)):
#                 ans+=abs(s[j]-s[j-1])
#     print(ans)