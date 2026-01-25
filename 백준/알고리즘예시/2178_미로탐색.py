# 최단 거리를 구하는 문제이기 때문에 BFS를 써서 풀어 볼 것임
# 길찾기 문제라서 이렇게 해봤다고 함
from collections import deque

dy = (0,1,0,-1)
dx = (1,0,-1,0)
N,M = map(int, input().split())
board = [input() for _ in range(N)] #좌표값 101010 이런식으로 주이질 때 저장할 리스트

def is_valid_coord(y,x): # 상,하,좌,우 범위 체크
    return 0 <= y < N and 0 <= x < M

def bfs():
    chk=[[False] * M for _ in range(N)] #체크 배열 갔던 부분인지 아닌지 판단하기 위함
    chk[0][0] = True
    dq = deque()
    # dq.append((0,0)) #원래 이렇게 나옴 (좌표값만 표시되어 있음)
    dq.append((0,0,1)) # 몇칸을 지나왔는지 알기 위해 마지막에 0추가 해줌 count용도 -> 그러나 처음부터 세는 걸로 문제에 나왔기 때문에 1로 시작함
    while dq:
        y,x,d = dq.popleft()
        if y == N-1 and x == M-1: #우 하단에 도착했을 때(끝날 때)
            return d
        nd= d+1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if is_valid_coord(ny,nx) and board[ny][nx] =='1' and not chk[ny][nx]: #1이고 방문을 하지 않았다면
                chk[ny][nx] = True
                dq.append((ny,nx,nd))

print(bfs())