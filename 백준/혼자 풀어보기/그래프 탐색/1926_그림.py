# 그래프 연습
#bfs로 풀면 되는 것 같은데
from collections import deque
n,m=map(int,input().split())
adj=[list(map(int,input().split())) for _ in range(n)]
# adj=[list(map(int,input().split())) for _ in range(N)]
# print(adj)
visited=[[0] * m for _ in range(n)]
def bfs(x,y):
    d=deque()
    d.append((x,y))
    visited[x][y]=1

    area = 1 # 넓이 저장 변수
    while d:
        r,s=d.popleft()
        for k,z in [(-1,0),(1,0),(0,1),(0,-1)]:
            dx,dy=r+k,s+z
            if 0<= dx < n and 0<= dy < m:
                if adj[dx][dy] == 1 and not visited[dx][dy]:
                    visited[dx][dy]=1
                    d.append((dx,dy))
                    # print(d)
                    area+=1 # 몇개의 간을 방문했는지 세면 그게 넓이
    return area
cnt=0
max_area=0
for i in range(n):
    for j in range(m):
        if adj[i][j]==1 and not visited[i][j]:
            ma=bfs(i,j)
            cnt+=1
            max_area=max(max_area,ma)
print(cnt)
print(max_area)
# print(*d)
# 여기까지 는 구했는데 넓이를 어떻게 구하지? -> Bfs 안에서 area 변수 활용해서 구함
# 참고 많이 해서 품.. 