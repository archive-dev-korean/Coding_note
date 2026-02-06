# 구현
# N=int(input())
# M=int(input())
# arr=[[0]*N for _ in range(N)]
# # print(arr)
# for i in range(1,N+1):
#     if N % 2>0:
#         arr[round(N)-1][round(N)-1] = 1 
#         arr[round(N)-1][round(N)-1 - i] = i+1
#         if len()
#     else:
#         arr=arr[round(N)][round[N]] = 1

# 분기 처리하면 에바임 못구함
# 패턴을 정해서 그걸 적용하면 됨
import sys
input=sys.stdin.readline
N=int(input())
M=int(input())
arr=[[0]*N for _ in range(N)]

# 하, 우, 상, 좌 순서로 이동함 (0,0) 기준으로
dx = [1,0,-1,0] #x의 좌표에 계산하면 아래,위쪽으로 됨
dy = [0,1,0,-1] #y의 조표 계산하면 오른쪽, 왼쪽으로 됨
x,y =0,0
d=0
num=N * N
tx = ty = -1 # M의 좌표?
while num > 0:
    arr[x][y] = num # 0,0에 49
    if num == M:
        tx,ty = x,y
    num -= 1
    if num==0:
        break
    nx = x + dx[d]
    ny = y + dy[d]
    # 다음 칸이 막히면 방향 전환
    if not (0<= nx < N and 0<= ny <N) or arr[nx][ny] !=0:
        d = (d+1) % 4
        nx = x + dx[d]
        ny = y + dy[d]

    x,y = nx, ny
    # 출력
out=[]
for i in range(N):
    for j in range(N):
        print(arr[i][j], end=' ')
    print()
print(tx +1, ty +1)