# 그래프 연습
from collections import deque
F,S,G,U,D=map(int,input().split())
# adj=[[0] * F for _ in range(F)]
visited=[0] * (F+1) # 방문 노드 기록 저장 인 동시에 거리까지 확장 용도
# print(adj)
def bfs(start,now):
    d=deque()
    d.append(start)
    visited[start]=1 #여기서 처음에 1을 해줬음 예를 들면 애초에 처음층이 방문층이라 같으면 0이어야 하는데 1로 초기화 되어서 그럼
    while d:
        cur=d.popleft() # 여기 부분 변수화 하고
        if cur == now: #cur 변수 초기화
            return visited[cur] -1 # 이 조건 추가 해 줘야 함 그래서 -1 해주는 거임
        for nxt in (cur + U, cur - D): # 그 변수를 쓰고
            if 1 <= nxt <= F and visited[nxt] == 0: # nxt 조건을 수정해주고
                visited[nxt]=visited[cur]+1 #visited[cur] == cur까지 온 거리 거기에 +1 해주는 건 한칸 더 가서 거리 갱신임
                d.append(nxt)
    return 'use the stairs' #리턴값을 넣어줘야 함
print(bfs(S,G))
# cnt=0
# if bfs(S,G):
#     cnt+=1
# else:
#     print('use the stairs')

# 30% 정도 아쉽다 이거