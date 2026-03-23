# 그래프 연습
# 연결 요소 구하는 거랑 비슷한 것 같음
import sys
sys.setrecursionlimit(10**6)
while True:
    w,h=map(int,input().split())
    if w==0 and h==0:
        break
    else:
        # adj=[[0]*(w+1) for _ in range(h)]
        # print(*adj)
        # if w==1 and h==1:
        #     i=int(input())
        # else:
        visited=[[0] * w for _ in range(h)] 
        l=[list(map(int,input().split())) for _ in range(h)]
        # print(*l)
        # for i in range(len(l)):


        # l이 행렬로 받으니까 여기서 1이 되는 행 또는 열 기준으로 adj에 담으면 되는 건가?
        # 대각선 검사는 어떡해 함?

        #정답 아이디어
        #l자체를 행렬로 받으니까 여기서 노드랑 간선 파악하면 되는거고
        # 대각선 검사는 dr,dc 이용해서 구하는 건데 이게 좀 어렵고 이해가 잘 안가는 부분 
        # 일단 알려준대로 해봄

        #방향 판별을 위함(대각선 구하려고 이거 쓴거고)
        dr = [-1, -1, -1, 0, 0, 1, 1, 1]
        dc = [-1, 0, 1, -1, 1, -1, 0, 1]

        #dfs구현
        def dfs(r,c):
            # global cnt
            visited[r][c] =1 
            for k in range(8):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0<= nr < h and 0 <= nc < w:
                    if l[nr][nc] == 1 and not visited[nr][nc]:
                        dfs(nr,nc)
        cnt=0
        for i in range(h):
            for j in range(w):
                if l[i][j] == 1 and not visited[i][j]:
                    dfs(i,j)
                    cnt+=1
        print(cnt)
# dfs로 풀면 Recursion error 나는 것 같으니
#bfs로 풀어야 하나? -> 제일 합리적 선택
from collections import deque

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]

    def bfs(sr, sc):
        q = deque()
        q.append((sr, sc))
        visited[sr][sc] = 1

        while q:
            r, c = q.popleft()

            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    if i == 0 and j == 0:
                        continue

                    nr = r + i
                    nc = c + j

                    if 0 <= nr < h and 0 <= nc < w:
                        if graph[nr][nc] == 1 and not visited[nr][nc]:
                            visited[nr][nc] = 1
                            q.append((nr, nc))

    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i, j)
                count += 1

    print(count)

# 결국 이 문제의 핵심은 좌표를 하나의 노드로 두고 좌표를 기준으로 연결된 좌표를 세면 되는거였음 즉 노드=(0,1) 같은 개념
# 이게 실버 2? 골드 정도는 되야 할 것 같은데