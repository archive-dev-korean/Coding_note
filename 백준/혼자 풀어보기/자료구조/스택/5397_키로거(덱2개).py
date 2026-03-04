# 자료구조 연습
# T=int(input())
# stk=[]
# for _ in range(T):
#     L=list(input())
#     print(L)
#     for i in range(len(L)):
#         if i==0 and L[i]=='<':
#             continue
#         elif L[i]=="<":
#             # stk.append(L[i-1])
#             i-=1
#         elif L[i]=='>':
#             stk.append(L[i+1])
#             i+=1
#         elif L[i]=='-':
#             stk.pop()
#             print(1)
#         else:
#             stk.append(L[i])
#         print(stk)
# 풀다보니 list보다는 deque이 조금 더 쉽다는걸 꺠달음
from collections import deque
import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    L=list(input().strip()) #strip 안쓰면 틀림
    # 이제 여기서 deque을 두개 써서 풀어야 함
    # left -> 커서 왼쪽 문자들, 값을 저장할 덱
    # right -> 커서 오른쪽 문자들
    # d=deque()
    left=deque()
    right=deque()

    for i in L:
        if i=="<":
            if left: #left에 값이 있으면
                right.appendleft(left.pop())
        elif i=='>':
            if right:
                left.append(right.popleft())
        elif i=='-':
            if left:
                left.pop()
        else:
            left.append(i)
            
    print(*(left+right),sep='')