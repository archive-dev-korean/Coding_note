# 자료 구조 연습
import heapq as hq

N=int(input())
l=[]
# result=[]
for _ in range(N):
    i=list(map(int,input().split()))
#     l.append(i)
# # print(l)
# for x in range(N):
#     for y in range(len(l)):
#         hq.heappush(result,-l[x][y])
#         # print(result)
# result.sort()
# print(-result[N-1])

# 이렇게 풀면 메모리 초과 뜨기도 하고 heap쓰는 의미가 없어짐

# min-heap을 활용한 풀이
    for x in i:
        if len(l) < N: #heap 에 아무겄도 없을경우 임
            hq.heappush(l,x)
        else:
            if x>l[0]:
                hq.heappop(l)
                hq.heappush(l,x)
print(l[0]) #루드 값 = 상위 N개에서 가장 작은 값 = N번째 큰수