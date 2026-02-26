# 자료구조 연습
import heapq as hq
pq=[]
N=int(input())
for _ in range(N):
    x=int(input())
    if x >0:
        hq.heappush(pq,x)
    elif x==0 and len(pq)==0:
            print(0)
    else:
        print(pq[0])
        hq.heappop(pq)