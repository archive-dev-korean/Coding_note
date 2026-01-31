# 누적합 연습
import sys
input=sys.stdin.readline
N,M = map(int,input().split())
a=[]
y=list(map(int,input().split()))
for x in y:
    a.append(x)
# a.append(i)
# for _ in range(N):
#     a.append(i)
# print(a)
# prefix=[0] * N
# prefix[0]=a[0]
# for z in range(1,N):
#     prefix[z] = prefix[z-1] + a[z]
s=0


# 이렇게 prefix[0] 이면 a[0]이렇게 넣으도 되긴 하지만
prefix=[0] *(N+1)
for i in range(1,N+1):
    prefix[i] = prefix[i-1] + a[i-1]
# 이렇게 누적합 배열이 적용 되고
# 부분합 구할 때는 그러면 편하게
#가능
for _ in range(M):
    i,j=map(int,input().split())
#     # 여기서 if 처리 해줘야 함. 헷갈리면 메모장에 a랑 prefix랑 적으면서 각각 규칙이 어떤건지 찾으면 됨.
#     if i == 1:
#         s = prefix[j-1]
#     else:
#         s = prefix[j-1] - prefix[i-2]
# s=prefix[j] - prefix[i-1]
#     print(s)
    s=prefix[j] - prefix[i-1]
    print(s)