# 자료구조 연습
from collections import deque
d=deque()
result=[]
N=int(input())
i=list(map(int,input().split()))
# d.append(i for i in range(1,N+1))
# for j in range(1,N+1):
#     d.append(j)
# print(d)
# print(i)
# print(x for x in d)
# 전형적인 rotate 문제인데 아까 푼 것 참고해서 함 풀어보기
# result.append(d.popleft())
# for x in range(len(i)):
#     if i[x]>0:
#         for _ in range(x-1):
#             d.append(d.popleft())
#             x=d[0]-1
#     result.append(d.popleft())
#     if i[x]<0:
#         for _ in range((-x)-1):
#             d.appendleft(d.pop())
#             x=d[0]-1
#     result.append(d.popleft())
# print(result)

# 음 일단 여기서 deque에 (번호,이동값) 을 적용해서 풀어야 함 -> 그래야 다음 이동 값을 구할 수 있으니
# 이거에 맞게 수정하면
for j in range(1,N+1):
    d.append((j,i[j-1])) # 이렇게 튜플 형식으로 저장 해야함
while d:
    num,move=d.popleft()
    result.append(num)

    if not d: #deque이 비었으면
        break 
    if move > 0:
        # 위에 이미 하나 뽑았으니 move-1번 왼쪽 회전
        for _ in range(move-1):
            d.append(d.popleft())
    else: # move가 음수 일 때
        # -move번 오른쪽 회전
        for _ in range(-move):
            d.appendleft(d.pop())
print(*result)

# 아이디어는 맞았는데 구현 과정에서 틀림 ㅅㅂ 일단 deque에 튜플 형태로 저장하는 것도 틀렸고 
# 이것만 좀 제대로 할 줄 알았다면 풀 었을 수도??