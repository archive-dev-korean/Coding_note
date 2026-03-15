# 스택, 큐 동시 연습
import sys
from collections import deque
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
d=deque()
result=[]
structure=[]
# for i in B:
#     d.append(i)
# print(d)
# ㅅㅂ 문제 이해가 잘 안가는데???????
# queue는 pop -> 제일 앞에 값
# Stack은 pop -> 제일 뒤에 값
# 이거 어렵다

M=int(input())
C=list(map(int,input().split()))

# for x in range(len(C)):
#     if A[x]==0: #큐일때 
#         d.appendleft(C[x])
#         result.append(d.pop())
#     elif A[x]==1:#스택일때
#         d.appendleft(C[x])
#         result.append(d.popleft())
# print(result)

# 스택과 큐 모두 고려한 구현

# for i in range(N):
#     if A[i]==0: # queue 일 때
#         structure.append(deque([B[i]]))
#     else:
#         structure.append([B[i]])
# for x in C:
#     cur=x
#     for i in range(N):
#         if A[i]==0:
#             structure[i].append(cur)
#             cur=structure[i].popleft()
#         else:
#             structure[i].append(cur)
#             cur=structure[i].pop()
#     result.append(cur)
# print(result)

# 하지만 이 문제는 queue일 때만 고려하면 됨 스택은 들어간게 그대로 나오기 떄문에 큐 일때 순서만 조심해서 구현하면 됨
# 그리고 이렇게 하면 시간 초과 남

# 큐만 고려한 구현
for i in range(N):
    if A[i]==0:
        d.append(B[i])
for x in C:
    d.appendleft(x)
    result.append(d.pop())
print(*result)