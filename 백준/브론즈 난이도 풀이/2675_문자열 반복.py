# 연습
N=int(input())
# print(ord(N))
for _ in range(N):
    i,j = input().split()
    for k in j:
        print(k*int(i),end='')
    print()