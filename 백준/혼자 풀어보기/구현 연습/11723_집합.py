# 구현 연습
import sys
input=sys.stdin.readline
M=int(input())
s=set()
for _ in range(M):
    i=input().split()
    if i[0] =='add':
        s.add(int(i[1]))
    elif i[0] =='check':
        if int(i[1]) in s:
            print(1)
        else:
            print(0)
    elif i[0] == 'remove':
        if int(i[1]) in s:
            s.remove(int(i[1]))
        else:
            continue
    elif i[0] == 'toggle':
        if int(i[1]) in s:
            s.remove(int(i[1]))
        else:
            s.add(int(i[1]))
    elif i[0] =='all':
        # s.replace(x for x in range(1,21)) 
        # replace 명령어 없어서 없애고 추가하는 방식으로 써야함.
        s.clear()
        s.update(int(x) for x in range(1,21))
    else:
        s.clear()
# int(i[1])로 바꿔 주면 시간 초과 안남 
# 원래는 str 타입이라 비교하면 시간 초과 나는 듯