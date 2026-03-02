# 자료구조 연습
import sys
input=sys.stdin.readline
N=list(input().strip())
M=int(input())
l=[] #결과값을 담을 리스트
# print(N)
# # cursor=len(N)-1
# # l.append(N)
for _ in range(M):
    cmd=map(str,input().split())
#     if i=='L':
#         cursor-=1
#         if cursor==0:
#             continue
#     elif i=='D':
#         cursor+=1
#         if cursor==len(N)-1:
#             continue
#     elif i=='B':
#         l.pop(l[cursor-1])
#         if cursor==0:
#             continue
#     elif i=='P':
#         l[cursor-1] = j
# # print(l)
    if cmd[0]=='L':
        if len(N)>0:
            l.append(N.pop())
        elif cmd[0]=='D':
            if len(l)>0:
                l.append(l.pop())
        elif cmd[0]=='B':
            if len(N)>0:
                N.pop()
        elif cmd[0]=='P':
            N.append(cmd[1])
print(N+l[::-1])