#연습
import sys
input=sys.stdin.readline
d={1:[1], 2:[2,4,8,6],3:[3,9,7,1],4:[4,6],5:[5],6:[6],7:[7,9,3,1],8:[8,4,2,6],9:[9,1]}

T=int(input())
for _ in range(T):
    a,b=map(int,input().split())
    last=a%10
    if last==0:
        print(10)
    else:
        cycle=d[last]
        print(cycle[(b-1)%len(cycle)]) #b번쨰는 (b-1) 인덱스
        # print((a**b)%10)
# 딕셔너리 안만들고 값을 구하려고 하면 시간초과 발생함
# 이렇게 주기성을 띈다는 것은 알았는데 -> 이걸 어떻게 처리하지? 약간 이 생각이 많이 들어서 당황함
