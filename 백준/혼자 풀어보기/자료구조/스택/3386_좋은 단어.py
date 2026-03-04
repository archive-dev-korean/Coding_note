# 자료 구조 연습
N=int(input())
cnt=0
for _ in range(N):
    stk=[]
    i=input()
    for x in i:
        if len(stk)==0:
            stk.append(x)
        else:
            if stk[-1]==x:
                stk.pop()
            else:
                stk.append(x)
    if len(stk)==0:
        cnt+=1
    else:
        pass
print(cnt)
# 이걸 왜 못풀지...???? 제발 아 ㅅㅂ 