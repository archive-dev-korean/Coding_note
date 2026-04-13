# 그래프 연습
# BFS
from collections import deque
def bfs(now):
    cnt=0
    d=deque()
    d.append(now)
    visited[now]=1
    while d:
        cur=d.popleft()
        for nxt in range(1,N+1):
            if adj[cur][nxt]==1 and visited[nxt]==0:
            # if adj[cur][nxt]==1:
                visited[nxt]=1
                cnt+=1
                d.append(nxt)
    return cnt
T=int(input())
for _ in range(T):
    N,M=map(int,input().split())
    adj=[[0] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        a,b=map(int,input().split())
        adj[a][b]=adj[b][a]=1
    # print(adj)
    visited=[0] * (N+1)
    print(bfs(a))
