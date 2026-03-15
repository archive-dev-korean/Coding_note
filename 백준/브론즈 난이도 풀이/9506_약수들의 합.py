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
