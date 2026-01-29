# 구현 연습
# 완전 탐색 쓰는 것(재귀)
N = int(input())
l=[]
result=[]
rank = [1] * N
for _ in range(N):
    i,j=map(int,input().split())
    # i=input().split()
    l.append((i,j))
# print(l)
#     if max(i[0][0]) and max(i[1][1]):
#         l.append(1)
#     elif min(i[0][0]) and min(i[0][1]):
#         l.append(N)
#     else:
#         l.append(2)
# print(l)

# 여기서 부터 완전 탐색으로 풀어야 함
for k in range(N):
    for s in range(N):
        if k==s:
            continue
        if l[k][0] < l[s][0] and l[k][1] < l[s][1]:
            rank[k] += 1
print(*rank)

# 완전 탐색 (재귀로 짜는 거임)
# k랑 s랑 비교해서 같으면 넘어가는 로직은 알아 둘 필요가 있을 것 같음 많이 써 먹을듯.