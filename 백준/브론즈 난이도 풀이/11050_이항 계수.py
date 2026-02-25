# 연습
from itertools import combinations
N,K=map(int,input().split())
print(len(list(combinations(range(N),K))))
# m=0
# total=0
# print(type(N
# l=[]
# l.append(N,K)
# print(l)
# for i in combinations(N,K):
#     print(i)
# for i in range(K):
#     m=N*(N-1)
#     N-=1
#     print(m)
# total=N//K  
# print(total)

#직접 구현
result=1
for i in range(K):
    result=result*(N-i)//(i+1)
print(result)