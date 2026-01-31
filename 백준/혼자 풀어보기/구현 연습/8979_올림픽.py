# 구현 연습
N,K = map(int,input().split())
a=[]
result=dict()
for _ in range(N):
    i=list(map(int,input().split()))
    a.append(i)
# print(a)
for j in a:
    r1=max(j[1])
    r2=max(j[2])
    r3=max(j[3])
    if j[1] ==r1:
        if j[2]==r2:
            result.append(j[0])
    elif 
    # if j[0] ==K:
    #     for l in j:
            

        
# 흠 전반적으로 다 틀려서
# 딕셔너리 쓰면서 구하는 밥
for _ in range(N):
    c,g,s,b=map(int,input().split())
    result[c] = (g,s,b)
rank=1
for k,v in result.items():
    if v > result[K]: #튜플 형태로 저장 되는데 파이썬은 알아서 처음,다음,그다음 이렇게 비교해줌 *****
        rank+=1
print(rank)