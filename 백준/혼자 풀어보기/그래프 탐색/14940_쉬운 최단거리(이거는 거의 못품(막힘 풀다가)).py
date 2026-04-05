# 구현 연습
from collections import deque
n,m=map(int,input().split())
# for _ in range(n):
a=[list(map(int,input().split())) for _ in range(n)]
# print(*i)
dist=[[-1] * m for _ in range(n)] # 결과 배열
# 시작점 정의
sx,sy=0,0
for i in range(n):
    for j in range(m):
        if a[i][j]==0:
            dist[i][j]=0
        elif a[i][j]==2:
            sx,sy= i,j

def bfs(x,y):
    d=deque()
    d.append((x,y))
    dist[x][y] =0 #여기서 초기회 해줌 (초기값(좌표 값이 2일때))
    while d:
        r,s=d.popleft()
        for w,z in [(0,1),(0,-1),(1,0),(-1,0)]:
            dx,dy=r+w,s+z
            if 0<= dx < n and 0<= dy < m:
                # if i[dx][dy]==1 and i[x][y]==2:
                #     d.append((dx,dy))
                if a[dx][dy] !=0 and dist[dx][dy] == -1: #a배열에서 0이 아닐떄만 검사 하고 방문하지 않았다면
                    dist[dx][dy] = dist[r][s] + 1
                    d.append((dx,dy))
bfs(sx,sy)

for k in dist:
    print(*k)


# 흠 아예 이해 못할 건 아닌 것 같은데 좀 어렵네