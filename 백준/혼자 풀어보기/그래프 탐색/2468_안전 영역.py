# 그래프 연습
from collections import deque
# d=deque()
N=int(input())
#bfs로 푸는 것 같은데
V=[list(map(int,input().split())) for _ in range(N)]
# print(V)
# for i in range(len(V)):
#     for j in range(len(V)):
#         d.append((i,j))
def bfs(a,b,num): # a,b -> 잠긴 칸, num=침수 높이
    d=deque()
    d.append((a,b))
    #bfs 안에서 deque 설정해서 넣는게 더 좋을 것이고(시작점 때문에)
    visited[a][b]=1 #방문 좌표 기록인데 이게 왜 필요하지 -> 기존처럼 0 으로 바꿔 버리면 나중에 V에서 판별을 못함
    while d:
        x,y=d.popleft()
        for k,r in [(0,1),(0,-1),(1,0),(-1,0)]:
            dx,dy=x+k,y+r
            # for k in range(len(V)):
            #     for l in range(len(V)):
            #         if 0< V[k][l] and V[k][l]<=num:
            #             V[k][l]=0 #방문처리
            #             if 0<=dx<N and 0<=dy<N and V[dx][dy]<=num:
            #                 d.append((dx,dy))
            if 0<= dx < N and 0 <= dy <N:
                if visited[dx][dy] == 0 and V[dx][dy] > num: #방문 한 적 없고 V의 좌표값이 침수 높이보다 높다면
                    visited[dx][dy]=1
                    d.append((dx,dy)) # 그 좌표 기록
        
#최종값을 구할 땐
result=[]
for x in range(0,101): # 침수 범위 아무것도 잠기 않았을 때도 있다고 했으니 1부터가 아니라 0부터
    visited=[[0] * N for _ in range(N)]
    cnt=0

    for i in range(N):
        for j in range(N):
            if V[i][j] > x and visited[i][j]==0:
                bfs(i,j,x)
                cnt+=1
    result.append(cnt)
    #결과를 담을 변수에 넣고(리스트가 될 것 같음)

print(max(result)) #변수(리스트)의 max값 출력인데