# 연습
# 1 2 3 4 5
# 2 1 3 4 5
# 2 1 4 3 5
# 3 1 4 2 5
# 3 4 1 2 5

N,M=map(int,input().split())
l=[x for x in range(1,N+1)]
# result=[0] * N
for _ in range(M):
    i,j=map(int,input().split())
    # l[i]=l[j]
    # result[j-1]=l[i-1]
    # result[i-1]=l[j-1]
    # l[j]=l[i]
    # print(l)
# idx=0
    # print(result)
    l[i-1:j] = l[i-1:j][::-1] # 아 ㅅㅂ
print(*l)

# 슬라이싱 쓰면 되는 문제였네....
