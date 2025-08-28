n,k = map(int, input().split())
def solution(n,k):
    list=[]
    s=1
    for i in range(1, n+1):
        if n % s ==0:
            list.append(s)
        s += 1
    if len(list) < k:
        return -1
    else:
        return list[k-1]
   
print(solution(n,k))

#리스트 활용함
