# DFS, BFS 연습
import sys
from collections import deque
N,M,V=map(int,input().split())
adj=[[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    v1,v2=map(int,input().split())
    adj[v1][v2]=1
    adj[v2][v1]=1 # 무방향 그래프는 서로 연결 되어 있어서 이것도 정의 해줘야함
# print(adj)
# for i in adj:
#     print(i)
def dfs(now):
    visited[now]=1 # 방문한 노드 기록(무방향이라 양쪽 다 연결 되어 있어서 하나의 노드 방문 했으면 체크 해둬야함)
    print(now,end=' ')
    for nxt in range(1,N+1):
        # if adj[now][nxt]:
        if adj[now][nxt] and not visited[nxt]:
            dfs(nxt)
            
def bfs(now):
    d=deque()
    d.append(now)
    visited[now]=1
    while d:
        now=d.popleft()
        print(now,end=' ')
        for nxt in range(1,N+1):
            # if adj[now][nxt]: #now에서 nxt가는 노드가 존재한다면
            if adj[now][nxt] and not visited[nxt]: #now에서 nxt가는 노드가 존재하고 방문하지 않았다면
                visited[nxt]=1
                d.append(nxt)
visited=[0] * (N+1) # 방문 체크 리스트 -> 방문한 노드 있으면 노그 값 저장됨
dfs(V)
print()
visited=[0] * (N+1) #dfs에서 썻으니 다시 정의 해줘야함
bfs(V)