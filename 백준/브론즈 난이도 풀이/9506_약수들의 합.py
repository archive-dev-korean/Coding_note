# 연습
while True:
    result=[]
    i=int(input())
    if i==-1:
        break
    else:
        for x in range(1,i):
            if i%x==0:
                result.append(x)

        if sum(result)==i:
            # print() 부분 출력형식만 맞추면 통과 join 쓰는것 좀 알아야 겠네
            print(f"{i} = ",end="")
            print(" + ".join(map(str,result)))
                # for y in range(1,len(result)):
                #     print(f"{i}="+result[0]+"{result[y]}")
        else:
            print(f"{i} is NOT perfect.")
# 근데 더 빨리 풀수 있는 방법은 루트를 쓰는 방법임
import math

while True:
    n = int(input())
    if n == -1:
        break

    div = [1]

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            div.append(i)
            if i != n // i:
                div.append(n // i)

    div.sort()

    if sum(div) == n:
        print(f"{n} = " + " + ".join(map(str, div)))
    else:
        print(f"{n} is NOT perfect")