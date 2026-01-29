# 구현 연습
# 큐 구조 써서 땡기고 없애고 하면 될 것 같음
from collections import deque
d=deque()
result=[]
N,K = map(int,input().split())
for i in range(1,N+1):
    d.append(i)
while len(d) > 0:
    for _ in range(K-1):
        pl=d.popleft()
        d.append(pl)
        # d.append(d.popleft())
    result.append(d.popleft())
    # ans=d.remove(d[K-1])

    # result.append(ans)
# print(result)
print("<" + ", ".join(map(str, result)) + ">")