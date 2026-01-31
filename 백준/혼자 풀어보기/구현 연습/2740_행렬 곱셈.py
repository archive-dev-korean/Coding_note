# 구현 연습
N,M=map(int,input().split())
A=[]
B=[]
for _ in range(N):
    i= list(map(int,input().split()))
    # for x in i:
    A.append(i)
# print(A)
X,Y=map(int,input().split())
result=[[0]*Y for _ in range(N)] #N행 Y열
for _ in range(X):
    j=list(map(int,input().split()))
    B.append(j)
if X==M:
    # result= A * B
    # 곱셈 식 다시 적음
    for i in range(N): #A의 행
        for j in range(Y): #B의 열
            for k in range(M): # 공통 차원
                result[i][j] += A[i][k] * B[k][j]

for r in result:
    for s in r:
        print(s, end=' ')
    print() #줄바꿈

# 행렬의 곱셈
# N행 M열의 행렬과 M행 Y열의 행렬을 곱하면
# N행 Y열의 행렬이 나옴