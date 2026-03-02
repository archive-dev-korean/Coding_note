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
    cmd=input().split()
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
        else:
            continue
    elif cmd[0]=='D':
        if len(l)>0:
            N.append(l.pop())
        else:
            continue
    elif cmd[0]=='B':
        if len(N)>0:
            N.pop()
        else:
            continue
    elif cmd[0]=='P':
        N.append(cmd[1])
print(*(N+l[::-1]),sep='')

# POP 을 이용해서 새로운 리스트에 값을 담거나 기존 리스트에 값을 추가하면서 푸는 문제임
# 스택 2개를 이용해서 푸는거임
# >>> 제발 이런 생각좀 해봐라 진짜.