# 그리디 브론즈 풀이
T=int(input())
time=[300,60,10]
answer=0
if T%10 !=0:
    print(-1)
else:
    for i in time:
            answer=T//i
            T%=i
            # if T%i != 0:
            #     print(-1)
            # else:
            #     print(answer)
            print(answer,end=' ')