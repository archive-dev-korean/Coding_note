# # 그래프 연습
import sys
from collections import deque
input=sys.stdin.readline
N,K=map(int,input().split())
# # 행렬로 구현 가능한가 이거??? -> 안될 것 같아서 인접 리스트 사용으로 수정
# adj=[[0]*1000000]
# adj[N]=adj[K]=1
# graph = [[] for _ in range(1000001)]
# graph[N].append(1)
# graph[K].append(1)
# # print(*graph)
# visited = [0] * (N+1) # 방문노드 
# 인접 행렬, 리스트 모두 쓰면 메모리 초과 날거임 100% 


#BFS로 푸는 것 같은데 -> 이건 맞음
# 다만 로직이 잘못 되었음
# GPT 참고 해서 품
# def bfs(now):
#     d=deque()
#     d.append(now)
#     while d:
#         now=d.popleft()
#         for nxt in range(1000001):
#             if graph[now]:
#                 d.append(nxt)
def bfs(start,target):
    visited=[-1] * 100001 #방문 한곳 체크 하기 위한 리스트 -1로 초기화 하는게 나중에 처리할 떄 편함
    d=deque()
    d.append(start)

    visited[start]=0

    while d:
        now=d.popleft()
        if now==target:
            return visited[now]
        
        for nxt in (now - 1, now + 1, now * 2):
            if 0<= nxt <= 100000 and visited[nxt] == -1: #여기서 한 번만 방문하게 함
                visited[nxt] = visited[now] + 1
                d.append(nxt)
print(bfs(N,K))

# 이해는 했는데 다시 나혼자 풀라고 하면 풀 수 있을 까..?