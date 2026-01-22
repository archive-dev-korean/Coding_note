# 맨 앞의 값을 삭제
# 맨 앞의 값을 맨 뒤로 보내기 _> 삭제 ,삽입---> O(N) 임
# 시간 복잡도 고려해서 기본 배열 구조로는 풀 수 없음
# 그래서 결론은 큐 구조로 풀 수 있음 -> O(1)

from collections import deque

dq = deque()
N = int(input())
for i in range(1, N+1):
    dq.append(i)
while len(dq) >1:
    dq.popleft()
    dq.append(dq.popleft())
# print(dq)
print(dq.pop())

# # 배열로 풀 경우 -> 시간 초과
# N = int(input())
# arr =[]
# for i in range(1, N+1):
#     arr.append(i)
# while len(arr) >1:
#     arr.pop(0)
#     arr.append(arr.pop(0))
# print(arr.pop())