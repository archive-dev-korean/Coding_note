# 구현 연습
from collections import deque
d=deque()
result=[]
N,K = map(int,input().split())
for i in range(1,N+1):
    d.append(i)
# print(d)
while len(d) > 0:
    for _ in range(K-1):
        pl=d.popleft()
        d.append(pl)
    result.append(d.popleft())
# print(result)
print("<" + ", ".join(map(str, result)) + ">")