# 자료구조 연습
from collections import deque
d=deque()
N,M=map(int,input().split())
p=list(map(int,input().split()))
# print(p)
ans=0
for i in range(1,N+1):
    d.append(i)
# print(d)
for j in p:
    idx=d.index(j)
    left = idx 
    right=len(d)-idx
    if left <= right:
        # 왼쪽으로 idx번 회전
        for _ in range(left):
            d.append(d.popleft())
            ans+=1
    else:
        # 오른쪽으로 len(d) - idx번 회전
        for _ in range(len(d) - idx):
            d.appendleft(d.pop())
            ans+=1
    d.popleft() #맨 앞 제거
print(ans)
    # if d[j+1]==j:
# 자료 구조 약한거 인정.. 연습해보자 ..
