# 연습
C=list(map(int,input().split()))
original=[1,1,2,2,2,8]
result=[]
# print(C)
# print(original-C)
for i in range(6):
    result.append(original[i]-C[i])

print(*result)