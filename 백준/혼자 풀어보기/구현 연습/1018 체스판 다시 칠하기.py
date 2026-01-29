# 구현 연습
N,M = map(int,input().split())
lst=[]
# 2차원 배열 만드려고 했는데 이렇게 하면 안되고
# for _ in range(N):
#     for _ in range(M):
#          i=input()
#          lst.append(i)
# print(lst)
for _ in range(N):
    row = list(input())
    lst.append(row)
# print(lst)
# for i in lst:

# 여기까지는 구했고
# 아이디어 
#1. 8x8로 자를 수 있는 모든 시작점 (i,j)을 돈다
# 2. 각 8x8 영역에서 두가지 경우를 비교
# 좌표의 합(r+c)의 짝/홀로 기대 색이 결정
# (r+c) 가 짝수 -> W
# (r+c) 가 홀수 -> B

# 패턴 비교(틀린 칸 세는 법)
#8x8 영역의 왼쪽 위를 (i,j)라고 할 때, 내부 칸은 (i+x,j+y)
# W가 시작 일 때 기대 색
# (x+y)%2==0 이면 W 아니면 B -> 처음 식은 인접한을 건너뛰었을 떄 W 아니면 B 라고 하는 식임
# B 일때는 반대로
ans=64
for i in range(N-7):
    for j in range(M-7):
        w_a =0 #(i,j)를 w로 시작한다고 가정했을 때, 다시 칠해야 하는 수
        w_b =0 #(i,j)를 b로 시작한다고 가정했을 때, 다시 칠해야 하는 수

        for x in range(8):
            for y in range(8):
                # w 시작 기준
                expected_w = 'W' if (x+y) % 2 == 0 else 'B'
                if lst[i+x][j+y] != expected_w:
                    w_a +=1
                
                # b 시작 기준
                expected_b = 'B' if (x+y) % 2 == 0 else 'W'
                if lst[i+x][j+y] != expected_b:
                    w_b +=1
        ans = min(ans, w_a, w_b)
print(ans)
