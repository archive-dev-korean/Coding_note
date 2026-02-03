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

# 부르트 포스로 푸는거 맞음 나중에 공부하고 다시 풀어보기
