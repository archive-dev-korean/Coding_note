# 그래프 연습
from collections import deque
N,M,K,X=map(int,input().split())
adj=[[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    A,B=map(int,input().split())
    adj[A][B]=1
# visited=[[0] * (N+1) for _ in range(N+1)]# 방문 체크
visited=[-1] * (N+1)# 거리 배열(visited 역할)
# visited=[]
# adj[X][]=1
# print(adj)
def bfs(start):
    d=deque()
    d.append(start)
    visited[start]=0 #거리 0부터 시작이라
    while d:
        now=d.popleft()
        for nxt in range(1,N+1):
            if adj[now][nxt] ==1  and visited[nxt]==-1:
                visited[nxt] = visited[now] +1
                d.append(nxt)
    # return now
bfs(X)
# found=False
for i in range(1,N+1):
    if visited[i] == K:
    # bfs(i)
        print(i)
        found = True
    # else:
if not found:
    print(-1)