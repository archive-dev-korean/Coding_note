# 구현 연습
from collections import deque
d=deque()
N=int(input())
a=[]
# d=[i for i in range(1,N)]
for i in range(1,N+1):
    d.append(i)
# print(d)
# d.pop()
# print(d)
while len(d)>1:
    a.append(d.popleft())
    d.append(d.popleft())
    # d.append(d.popleft())
    # print(d)
print(*a, d[0])
for x in a:
    print(x, end=' ')
print(d[0])