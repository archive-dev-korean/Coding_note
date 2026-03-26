# 그래프 연습(골드5)
# BFS로 푸는 거겠지??
# V,E=map(int,input().split())
from collections import deque
M,N=map(int,input().split())
# for _ in range(N):
    # for _ in range(H):
V=[list(map(int,input().split())) for _ in range(N)]
# print(V)
visited=[[0] * M for _ in range(N)]
# print(visited)
def bfs():
    # cnt=1
    d=deque()
    #큐에 처음 받은 토마토의 위치 좌표를 append 시킴
    for i in range(N):
         for j in range(M):
              if V[i][j] == 1:       
                d.append((i,j))
    # visited[now][nxt]=1
    while d: #여기서 부터 bfs로직 돌아감
        r,c=d.popleft()
        for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
            # if i == 0 and j == 0:
            #             continue
            nr= r+i #여기서 now -> r로 바꿔야 하고
            nc= c+j #여기서 nxt -> c로 바꿔야 함
            if 0 <= nr < N and 0 <= nc < M: #해당 좌표가 좌표 크기를 넘어가면 안되고
                        # if V[nr][nc] == 1 and not visited[nr][nc]:
                        #     visited[nr][nc] = 1
                            # cnt+=1

                if V[nr][nc] == 0: #그 좌표에 토마토가 익지 않은채로 있어야함
                    # 익히고 1을 더해주면서 횟수를 세어주기
                    # 여기서 나온 제일 큰 값이 정답임
                    V[nr][nc] = V[r][c] + 1 #현재 칸보다 하루 뒤에 익는다
                    d.append((nr, nc))
                        # elif V[nr][nc]==-1:
                        #       return -1
    # return cnt
        
# count = 0
# for i in range(N):
#     for j in range(M):
#         if V[i][j] == 1 and not visited[i][j]:
#             bfs(i, j)
#             count += 1

# print(count)
#마지막 로직이 틀렸는데

#이렇게 적어야 함
ans=0 # 정답이 담길 변수

bfs()#bfs 실행하고
for i in range(N):
      for j in range(M):
            if V[i][j]==0: #다 찾아봤는데 토마토를 익히지 못했다면 -1 출력
                  print(-1)
                  exit()
            ans=max(ans,V[i][j]) #다 익었다면 최댓값이 정답
print(ans -1) #처음 시작을 1로 표현해서 1을 빼줌


# 와 어렵네 이거....