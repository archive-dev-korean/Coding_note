# 구현 연습
# 우선순위 큐 쓰면 되는 것 같은데
import heapq as hq
pq=[]
T=int(input())
for _ in range(T):
    q=[]
    N,M =map(int,input().split())
    P = list(map(int,input().split()))
    # hq.heappush(pq,M)
    # for i in range(N):
    #     q.append((i,P[i]))
    # q = [(i, P[i]) for i in range(M)]
# 최대힙 만들기
#     pq = [-p for p in P]
#     hq.heapify(pq)
#     cnt =0

#     while q:
#         idx,p = q.pop(0) #리스트로 큐 처럼 활용

#         # 더 높은 중요도 남아있으면 뒤로
#         if p < -pq[0]:
#             q.append((idx,p))
#         else:
#             hq.heappop(pq)
#             cnt +=1

#             if idx == M:
#                 print(cnt)
#                 break
# # print(pq)

#아래 방식 처럼 직관적으로
# for _ in range(T):
#     N,M = map(int,input().split())
#     P= list(map(int,input().split()))

    # q=[]
    max_heap=[]

    for i in range(N):
        q.append((i,P[i]))
        hq.heappush(max_heap, -P[i])
    cnt=0
    while q:
        idx, p = q.pop(0)

        #중요도가 더 남아 있으면 뒤로
        if p< -max_heap[0]:
            q.append((idx,p))
            continue
        #출력 되는경우
        hq.heappop(max_heap)
        cnt+=1
        if idx==M:
            print(cnt)
            break