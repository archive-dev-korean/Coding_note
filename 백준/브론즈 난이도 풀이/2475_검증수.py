# 연습
N=list(map(int,input().split()))
# print(N)
result=0
for i in N:
    result+=i**2
    result=result%10
print(result)