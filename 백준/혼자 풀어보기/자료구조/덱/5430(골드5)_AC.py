# 골드 5 덱 풀이 연습
from collections import deque
d=deque()
import sys
input=sys.stdin.readline
T=int(input())

for _ in range(T):
    p=input().strip()
    n=int(input())
    # l=list(input().strip()[1:-1].split(','))
    arr=input().strip()[1:-1] #이 부분 도움 받음 -> 입출력에서 '[' ']' 지우기
    # d.append(l)
    # 여기서는 []로 들어 온다면 [''] 이렇게 저장 되는데 이걸 없애는 것
    # if arr=='':
    #     l=[]
    # else:
    #     l=arr.split(',')
    # # print(l)
    # for i in p:
    #     if i=='R':
    #         l[::]=l[::-1]
    #     elif i=='D':
    #         if len(l)==0:
    #             print('error')
    #             break
    #         else:
    #             l.pop(0)
    
    # if l:
    #     print('['+','.join(l)+']') #join 사용법 확인
    # else:
    #     pass

# 이렇게 풀면 시간 초과 발생 하니까 deque을 활용해 풀어야 함
    if arr=='':
        d=deque()
    else:
        d=deque(arr.split(','))
    rev=False # False = 뒤집혀 있지 않은 상태/ True = 뒤집혀 있는 상태
    ok=True

    for i in p:
        # 아래는 실제로 뒤집지 않고 논리적으로 뒤집었다고 가정하고 푼 로직
        if i=='R':
            rev=not rev #False -> True 뒤집힌 상태로 간주
                        #True -> False 정상 방향으로 간주
                        #실제 deque의 방향은 그대로
        else: # D인 경우
            if not d: #d가 비어있는 경우
                ok=False
                break
            if not rev: #rev ==False -> 정상 방향
                d.popleft() # False면 해당 수행
            else: # rev==True -> 뒤집한 상태
                d.pop() #뒤에서 삭제(뒤집한 상태의 '앞'에 대항)
    if not ok: #not 이 붙었기 때문에 ok 가 False에서 True로 바뀜
        print('error')
    else:
        if rev: #rev가 True면(즉 뒤집혀 있으면)
            d.reverse() #다시 뒤집어서 출력
        print('['+','.join(d)+']')

    # 와 개헷갈리네 Flag 문제 연습 많이 해야 겠따.