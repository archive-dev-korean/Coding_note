# 구현 연습
A,P=map(int,input().split())
D=[]
D.append(A)
seen={A}
# print(D)
i=0
j=1
while True:
    # if D[i] <= 99:
    #     t=D[i] // 10
    #     z=D[i] % 10
    #     total=t**P + z**P 
    #     # i+=1
    # else:
    #     h=D[i] // 100
    #     t=(D[i] % 100) // 10
    #     z=(D[i] % 100) % 10
    #     total=h**P + t**P + z**P
    x=D[i]
    total=0
    while x>0:
        total+=(x%10) **P
        x //= 10
    if total in seen:
        break
    # if total in D:
    #     break
    D.append(total)
    seen.add(total)
    i+=1
print(D.index(total))
# 아마 정답은 맞을 텐데 시간초과 발생함
# 시도 1 seen변수 추가 해봄
# 시도 2 D[i]를 변수화 해봄
# 최종 정답 처리 -> 시도1, 시도2 전부 써야 정답
