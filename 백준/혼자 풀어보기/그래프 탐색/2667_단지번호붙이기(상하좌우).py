# 그래프 연습
from collections import deque
N=int(input())
result=[] # 단지수를 담을 리스트
# for _ in range(N):
A=[list(map(int,input())) for _ in range(N)]
# print(A)
visited=[[0] * N for _ in range(N)] 
def bfs(sr,sc):
    cnt=1
    d=deque()
    d.append((sr,sc))
    visited[sr][sc] = 1
    # for i in range()
    while d:
        r,c=d.popleft()
        # for i in [-1,0,1]:
        #     for j in [-1,0,1]:
            # 이 두개의 for문은 대각선 탐색까지 포함하게 되어 있음
            # 상,하,좌,위 만 따지려면 여기서 if 조건문을 포함해사
                # if abs(i) + abs(j)==1: # 이 조건 추가하면 됨 아니면
        for i,j in [(-1,0),(1,0),(0,1),(0,-1)]: # 이렇게 정의 하던가
            # 4개의 방향 벡터를 하나씩 꺼내 쓰는건데
            # (i, j) ∈ {(-1,0), (1,0), (0,1), (0,-1)} 이렇게 되는 것


                # if i == 0 and j == 0:
                #         continue

            nr = r + i
            nc = c + j

            if 0 <= nr < N and 0 <= nc < N:
                    if A[nr][nc] == 1 and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        cnt+=1
                        # result.append(cnt)
                        d.append((nr, nc))
    return cnt

count = 0
for i in range(N): 
    for j in range(N): #여기까지 모든 노드 돌음
        if A[i][j] == 1 and not visited[i][j]: #아직 방문 안했으면
            size=bfs(i, j) #bfs시작 -> 연결된 것 전부 방문
            result.append(size)
            count += 1
            # result.append(count)

print(count)
result.sort()
for x in result:
    print(x)
