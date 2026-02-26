# 자료 구조 연습
import sys
import heapq as hq
input=sys.stdin.readline
N=int(input())
pq=[]
for _ in range(N):
    x=int(input())
    if x > 0:
        hq.heappush(pq,-x)
    elif x==0 and len(pq)==0:
        print(0)
    else:
        print(-pq[0])
        -hq.heappop(pq)
# 강의 들어서 알고는 있었는데 까먹었던거 기억해냄