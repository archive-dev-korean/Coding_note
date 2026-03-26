# 그래프 연습
from collections import deque
d=deque()

# bfs로 푸는거임
def bfs():
    while d:
        x,y=d.popleft()
        for k,r in [(0,1),(0,-1),(-1,0),(1,0)]:
            dx,dy=x+k,y+r
            if 0<=dx<N and 0<=dy<M and V[dx][dy]==1:
                # V[dx][dy] = V[x][y] + 1 
                V[dx][dy] =0 #방문 처리
                d.append((dx,dy))
T=int(input())
for _ in range(T):
    cnt=0
    M,N,K=map(int,input().split())
    # V=[list(map(int,input().split())) for _ in range(K)] #배추 좌표 목록이 주어짐 좌표 전체 지도 아님
    # 수정하면
    V=[[0] * M for _ in range(N)] #N개 행 M개의 열
    for _ in range(K):
        x,y=map(int,input().split()) #x=열(가로) ,y=행(세로)
        # V[x][y]=1 #V[행][열] 접근으로 가야함
        V[y][x]=1 #그래서 y,x 순으로 넣어여 함[행][열]접근
# for _ in range(K):
    # print(V)
    for i in range(N):
        for j in range(M):
            if V[i][j]==1:
                d.append((i,j))
                bfs() # bfs 실행 시키고
                cnt+=1
    print(cnt)
