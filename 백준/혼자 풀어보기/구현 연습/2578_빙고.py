# 구현 연습
Bingo=[]
speak=[]
for _ in range(5):
    N=list(map(int,input().split()))
    Bingo.append(N)
for _ in range(5):
    M=list(map(int,input().split()))
# Bingo.append(N)
    speak.extend(M)
    # print(M)
# print(Bingo)
# print(speak)

#빙고 줄 수 세는 함수
def count_bingo(board):
    lines=0
    for i in range(5):
        if all(board[i][j] == 0 for j in range(5)): #가로줄 세기
            lines+=1
    for j in range(5):
        if all(board[i][j] ==0 for i in range(5)): #t세로줄 세기
            lines+=1
    if all(board[i][i]==0 for i in range(5)): #죄측 위부터 우측 아래로 가는 대각선
        lines+=1
    if all(board[i][4-i]==0 for i in range(5)): #좌측 아래부터 우측 위까지 가는 대각선
        lines+=1
    return lines


# 여기서부터 부르는 숫자에 맞음녀 0으로 바꿔서 빙고수 출력 하는 걸로 가기로 생각함.
prefix=[[False] * 5 for _ in range(5)]
# print(prefix)
for idx,num in enumerate(speak):
    for i in range(5):
        for j in range(5):
            if Bingo[i][j] == num:
                Bingo[i][j]=0

    if count_bingo(Bingo) >=3:
        print(idx+1) # 몇 번째 숫자에서 3빙고 인지
        break
# for i,j in enumerate(리스트):
# 이면 i = 인덱스 값
# j= 값(요소)
# print(i,j) = 0 A , 1 B 이런식으로 나옴

# all(반복 가능한 것) -> 안에 있는 값이 전부 True 이면 True
# 하나라도 아니면 False

# any(반복 가능한 것) -> 안에 하나라도 True 이면 True
# 전부 False 이면 False