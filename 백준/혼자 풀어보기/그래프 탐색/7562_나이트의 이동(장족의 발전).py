#그래프 연습
from collections import deque
# bfs로 푸는것
def bfs(x,y,tx,ty): #x,y는 처음 좌표 , tx,ty=도달 좌표
    d=deque()
    d.append((x,y))
    visited[x][y]=1
    while d:
        r,c=d.popleft()

        #이 조건을 써줘야 도착 좌표에 도달 했을 때 끝남
        if r==tx and c==ty:
            return visited[r][c]
        
        for i,j in [(-2,-1),(2,-1),(2,1),(-2,1),(-1,2),(1,2),(-1,-2),(1,-2)]:
            dx,dy=r+i,c+j
            if 0<=dx < I and 0<= dy < I and visited[dx][dy]==0:
                        # visited[dx][dy]=1 # 여기서 방문체크만 하는 것이 문제
                        visited[dx][dy] = visited[r][c] +1 # 이렇게 고쳐 줘야함
                        d.append((dx,dy))
T=int(input())
L=[]
for _ in range(T):
    I=int(input()) #한변의 길이
    visited=[[0] * I for _ in range(I)] #방문 값 체크
    # cnt=0
    # for _ in range(2):
    a,b=map(int,input().split()) #처음 좌표
    c,d=map(int,input().split()) #도달 좌표
        # L.append((a,b))
    # cnt+=1
    # print(cnt)
    print(bfs(a,b,c,d)-1)



                    
