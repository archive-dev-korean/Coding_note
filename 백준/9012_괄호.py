# stack을 사용한 전형적인 문제
T = int(input())
for _ in range(T):
    stk=[]
    isVPS= True
    for ch in input():
        if ch=="(":
            stk.append(ch)
        else:
            # if len(stk)>0:
            if stk: #위에 비어 있는지 안 비어 있는지 아는 거랑 같은 결과 나옴
                stk.pop()
            else:
                isVPS= False
                # print('NO')
                break

    if len(stk) >0:
        isVPS = False
        # print("NO")
    # else:
    #     print('YES')
    print("YES" if isVPS else 'NO')