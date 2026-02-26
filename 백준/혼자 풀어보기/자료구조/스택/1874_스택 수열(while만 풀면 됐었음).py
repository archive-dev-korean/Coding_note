# 스택 연습
import sys
input=sys.stdin.readline
n=int(input())
l=[]
stk=[]
result=[]
for _ in range(n):
    i=int(input())
    l.append(i)
# print(l)

# for j in range(1,n+1):
#     stk.append(j)
#     print('+')
#     for k in l:
#         if j == k:
#             stk.pop(-1)
#             print('-')
#     # if stk.append(i):
#     #     print('+')
#     # elif stk.pop():
#     #     print('-')
#     print(stk)

# 하다보니 이렇게 하면 100% 시간 초과
# 도움 받아서 조금 고치면
idx=0 # l에서 현재 만들어야 할 수열 위치
for j in range(1,n+1):
    stk.append(j)
    # print('+')
    result.append('+')
    # 스택 top이 현재 만들어야 할 값이면 pop
    while stk and stk[-1] == l[idx]: # 여기서 stk and 이 조건 없으면 인덱스 에러
        stk.pop()
        # print('-')
        result.append('-')
        idx+=1
# if stk: # stk의 값이 남아있으면 불가능한 경우 임
    # print('NO')
if stk:
    print('NO')
else:
    print(*result,sep='\n')
    # 여기서 for i in result;
    # print(i) 했으면 느리고 시간 초과 날 수도 있음 result가 커지면

# 아 생각은 했는데 왜 구현을 못하지...
# while이 핵심인데 써볼까? 생각만 해봄 ㅅㅂ
# 근데 결국 출력 초과가 나는데
# 아 원인은 No 일 때도 +,- 가 출력되서 그런거였음
# result로 결과 남아서 출력하면 맞음