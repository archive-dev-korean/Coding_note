# 그래프 연습
N=int(input())
adj=[list(map(int,input().split())) for _ in range(N)]
# print(adj)
# dfs로 풀어도 될 것같은데 내생각은

# 결론 dfs bfs둘다 풀어도 풀림 여유가 되면 bfs로도 풀어보기

visited=[[0] * N for _ in range(N)] #방문 기록 겸 결과 출력 리스트 // 여기서 visited[i][j] = i에서 j로 도달 가능 이렇게 생각해야함
# def dfs(i,j):#dfs 구성이 좀 틀린 것 같은데
#     visited[i][j]=1
#     for nxt in range(N):
#         if adj[i][nxt]==1:
#             dfs(nxt)
#             if visited[nxt] == 1:

def dfs(start, now): #이렇게 구성하고(AI)
    # start = 처음 출발한 노드
    # now = 현재 서있는 노드
    for nxt in range(N):
        if adj[now][nxt] == 1 and visited[start][nxt] ==0:
            visited[start][nxt]=1
            dfs(start,nxt)

# 이 부분도 좀 틀린 것 같은데
# for x in range(len(adj)):
#     for y in range(len(adj)):
#         dfs(x,y) #이렇게 실행하고

# 이렇게 구성?(AI)
for i in range(N): #각 노드에서 출발해 경우를 한 번씩 다 보는 것
    dfs(i,i) #dfs(0,0) 이면 0에서 출발해서 지금 0에 있는 상태
for k in visited:
    print(*k)#결과를 출력하면 될 것 같은데??

# 결국에 좌표 탐색이 아니라 i에서 출발해서 어디까지 갈 수 있는지를 찾는 문제라서 도착점(j)를 미리 정해놓고 dfs하면 안됨