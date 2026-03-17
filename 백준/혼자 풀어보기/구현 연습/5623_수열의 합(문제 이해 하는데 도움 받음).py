# 구현(수학) 연습
# 흠 이거 문제는 이해 했는데 점화식? 구하는게 빡세네
N=int(input())
result=[]
S=[]
for _ in range(N):
    S.append(list(map(int,input().split())))
# print(S)
if N==2:
    print(S[0][1]//2, S[0][1]//2)
else:
    for i in range(N):
        j=(i+1)%N
        k=(i+2)%N
        val= (S[i][j] + S[i][k]- S[j][k]) // 2
        result.append(val)
    
    print(*result)

# 0  A1+A2  A1+A3
# A2+A1  0  A2+A3
# A3+A1  A3+A2  0
# 이렇게 N=3 주어진다면
# arr[i][j] = A[i] + A[j]

# A[1] + A[2] = S(1,2)
# A[1] + A[3] = S(1,3)
# A[2] + A[3] = S(2,3)
# +
# -----------------------
# A[1] = (S(1,2)+ S(1,3) - S(2,3)) //2

# 즉 A[i] = (arr[i][j]+ arr[i][k]-arr[j][k]) // 2