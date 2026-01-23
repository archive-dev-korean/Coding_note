# 우선순위 큐 쓰면 되는 것 같은데? Pyrhon은 어자피 min-heap이니까

import heapq as hq
import sys
input = sys.stdin.readline
T=int(input())
pq=[]
for i in range(T):
    
    n= int(input())
    # n = input() # 빠른 입출력 써야함 10만번 호출하기 때문에
    # 여기서 추가
    if n: # n이 0이 아닐 때 
        hq.heappush(pq,(abs(n),n)) #튜플 형태로 우선 순위 큐에 저장 
    else: # 0일 때
        if pq: # 비어 있지 않을 때
            # print(hq.heappop(pq)) # 튜플을 반환하기 때문에
            print(hq.heappop(pq)[1]) # 이렇게 하면 뒤에 있는 값만 나옴
        else: # 비어 있을 때,
            print(0)
        # 바로 위 if else를 한줄로 표현도 가능
        # print(hq.heappop(pq) if pq else 0)
   
   # 내가 시도 했던 것
    # hq.heappush(pq,n)
    # for j in n:
    #     if j == 0:
    #         print(hq.heappop(pq)

# sort로도 풀 수 있는 것 같음
# .sort()쓰면 오름차순으로 됨

#다른 방법 우선순위 위에는 튜플을 활용한 풀이 였고
# n을 우선순위 큐에 넣어서 푸는 방식도 있음

min_heap=[] # 양수 1,2,3,6,78,1233 등등
max_heap=[] # 음수 -1, -4, -10, -129 등등
for i in range(T):
    x = int(input)
    if x:
        if x>0:
            hq.heappush(min_heap,x)
        else:
            hq.heappush(max_heap,-x) # 최대 힙 처리
    else: # 0일 때 절댓값 비교,
        #경우가 4가지로 나뉨
        # 양수(min_heap)가 비어있고 음수가 비어 있는 경우 -> 0
        # 음수만 비어 있는 경우 -> min_heap의 루트 노드
        # 양수만 비어 있는 경우 -> max_heap의 루트 노드
        # 둘 다 비어 있는 경우 -> 절댓값 비교해서 작은 거, 같을 때는 max_heap[0]

        if min_heap: # 비어 있는 경우
            if max_heap:
                if min_heap[0] < abs(-max_heap[0]):
                    print(hq.heappop(min_heap))
                elif min_heap[0] > abs(max_heap[0]):
                    print(-hq.heappop(max_heap))
                else: # 둘의 절댓값이 같을 때
                    print(-hq.heappop(max_heap))

            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)