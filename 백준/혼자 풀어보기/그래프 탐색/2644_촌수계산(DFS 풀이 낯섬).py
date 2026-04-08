# 그래프 연습
# bfs dfs 둘다 풀릴 것 같은데
from collections import deque
n=int(input())
a,b=map(int,input().split())
m=int(input())
adj=[[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    x,y=map(int,input().split())
    adj[x][y]=adj[y][x]=1 #양방향 그래프임 단방향 인줄 알았는데
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
# bfs(a)

# if visited[b]==0:
#     print(-1)
# else:
#     print(visited[b]-1)

# DFS로도 아래에 구현 해보셈
answer=-1
def dfs(start,depth):
    global answer # 전역변수 사용하기 때문에 이거 선언 해주고
    if start==b: # 이 처음노드가 마지막 촌수와 같다면 그 촌수 출력하고
        answer=depth
        return
    
    visited[start]=1
    for nxt in range(1, n+1):
        if adj[start][nxt]==1 and visited[nxt]==0:
            # visited[nxt]=visited[start]+1
            # dfs(nxt)
            dfs(nxt,depth + 1) #다음 노드(촌수) 로 이동하면 depth도 늘어나니까 이렇게 +1 해줘야 알맞게 표시됨
dfs(a,0)
print(answer)