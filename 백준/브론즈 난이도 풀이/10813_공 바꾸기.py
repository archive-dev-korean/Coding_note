# 연습
N,M=map(int,input().split())
s=[] #초기 리스트
result=[]
for k in range(1,N+1):
    s.append(k)
for _ in range(M):
    i,j=map(int,input().split())
#     if j in s:
#         j=i
#         result.append(j)
# print(result)
# # print(s)
# for k in s:
#     if j==k:
#         j=k
# 리스트 교환
    s[i-1],s[j-1]=s[j-1],s[i-1]
print(*s)