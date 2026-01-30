# 구현 연습
from collections import deque
import sys
input=sys.stdin.readline
d=deque()
S=input().strip()

in_tag=False # 태그 있는지 없는지 상태 False = 태그 밖, 단어 뒤집기 필요
# True = 태그 안, 그대로 출력

# print(S)
for i in S:
    # if i != ' ':
    #     d.appendleft(i)
    if i == '<':
        # 태그 시작 -> 지금 단어 먼저 출력
        while d:
            print(d.popleft(),end='')
        in_tag =True
        # d.append(i)
        print(i,end='')
    elif i== '>':
        in_tag=False
        print(i, end='')
    elif in_tag:
            #태그 안 -> 그대로 출력
        print(i,end='')
    else:
        # 태그 밖
        if i ==' ':

        # break
        #공백을 만나면 popleft부터 출력
            while d:
                print(d.popleft(),end="")
            print(' ', end='')
        else:
            d.appendleft(i) 
            # 여기서 역순으로 저장하니까

    # d.appendleft(i)
# for _ in range(len(d)):
#     a=d.pop()
#     d.appendleft(a)
#     # break
for i in d:
    print(i, end='')