# 구현 연습
N=int(input())
oracle=[[0] * 3]
oracle2=[]
for j in oracle:
    for i in j:
        oracle2.append(i)
print(oracle2)
# print(oracle)
for _ in range(N):
    n,s,b=map(int,input().split())
    temp=[]
    