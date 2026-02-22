# 그리디 알고리즘 브론즈
T=int(input())
# c=[0.25,0.10,0.05,0.01] # 이걸 float말고 정수 단위로 바꿔야 함
c=[25,10,5,1]
answer=0
cnt=0
l=[]
for _ in range(T):
    i=int(input())
    l.append(i)
# print(l)
for x in l:
    result=[] #여기서 리스트 초기화 해줘야 각 값 마다 거스름돈 초기화 함
    for y in c:
        answer=x//y
        result.append(answer)
        x %= y
    print(*result)