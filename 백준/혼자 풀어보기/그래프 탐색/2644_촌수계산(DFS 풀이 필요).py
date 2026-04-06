# 그래프 연습
# bfs dfs 둘다 풀릴 것 같은데
from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
adj=[[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    adj[x][y]=adj[y][x]=1 #양바양 그래프임 단방향 인줄 알았는데
# print(*adj)
visited=[0] * (n+1)
def bfs(start):
    d=deque()
    d.append(start)
    visited[start]=1
    while d:
        now=d.popleft()
        for nxt in range(1,n+1):
            if adj[now][nxt]==1 and visited[nxt]==0:
                visited[nxt]=visited[now]+1
                d.append(nxt)
# for i in adj:
bfs(a)

if visited[b]==0:
    print(-1)
else:
    print(visited[b]-1)

# DFS로도 아래에 구현 해보셈