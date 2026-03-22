# 그래프 연습(골드5)
# BFS로 푸는 거겠지??
# V,E=map(int,input().split())
from collections import deque
M,N,H=map(int,input().split())
for _ in range(N):
    for _ in range(H):
        V=list(map(int,input().split()))
        # print(type(V))
def bfs(now,nxt):
    d=deque()
    d.append(now)
    while d:
        now=d.popleft()
        for nxt in range(1,M+1):
