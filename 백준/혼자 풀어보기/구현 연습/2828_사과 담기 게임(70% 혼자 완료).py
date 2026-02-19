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
N,M=map(int,input().split())
J=int(input())
s=[]
for _ in range(J):
    i=int(input())
    s.append(i)
L=1
R=M
ans=0
# for i in range(len(s)):
#     if s[i] > R:
#         ans+=abs(s[i] - R)
#     elif M==1:
#         for j in range(1,len(s)):
#             ans+=abs(s[j]-s[j-1])
# print(ans)
for x in s:
    if x<L:
        move=L-x
        ans+=move
        L-=move
        R-=move
    elif x>R:
        move = x - R
        ans+=move
        L+=move
        R+=move
print(ans)