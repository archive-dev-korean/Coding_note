# 자료구조 연습
from collections import deque
N=int(input())
q=[]
for _ in range(N):
    i=input().split()
#     l.append(i) 
    if i[0]=='push':
        q.append(i[1])
    elif i[0]=='pop':
        if len(q)==0:
            print(-1)
        else:
            print(q.pop(0))
    elif i[0] =='size':
        print(len(q))
    elif i[0] =='empty':
        if len(q) ==0:
            print(1)
        else:
            print(0)
    elif i[0]=='front':
        if len(q) ==0:
            print(-1)
        else:
            print(q[0])
    elif i[0]=='back':
        if len(q)==0:
            print(-1)
        else:
            print(q[-1])



# print(i[0])
# for j in range(N):
#     if 