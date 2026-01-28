# 해시 연습 난이도(골드2) 어려울걸?
# F = int(input())
# d=dict()
# for _ in range(F):
#     n= int(input())
#     for _ in range(n):
#         a,b = input().split()
#         d[a] = b

# # print(d)
# cnt=0
# for k,v in d.items():
#     if v==k:

# DSU로 푸는 것
# 근데 개념 모르니까 일단 안쓰고 풀어봄 -> 이해 하는데 좀 빡셈 내가 다시 써볼 수 있을지 모르겠음

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    F = int(input())
    net = {}

    for _ in range(F):
        a, b = input().split()

        if a not in net and b not in net:
            s = set([a, b])
            net[a] = s
            net[b] = s
            print(net.items())

        elif a in net and b not in net:
            net[a].add(b)
            net[b] = net[a]
            print(net.items())

        elif a not in net and b in net:
            net[b].add(a)
            net[a] = net[b]
            print(net.items())

        else:
            if net[a] is not net[b]:
                # 두 네트워크 병합
                merged = net[a] | net[b]
                for x in merged:
                    net[x] = merged
                    print(net.items())

        print(len(net[a]))
