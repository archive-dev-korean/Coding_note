# 구현 연습
import sys
input=sys.stdin.readline
N=int(input())
a=[]
for i in range(1,N+1):
    # i=int(input())
    a.append(str(i))
# print(a)
# for j in a:
#     # for k in range(len(N)):
#     #     if j // 10 ==k+1:
#     #         a[j] = 2
#     #     else:
#     #         a[j] = 1
#     a.append(''.join(a[j]))
# print(a)
#a의 원소 모두 이어 붙이기
s=''.join(a)
answer=0
# print(s)
# for j in s:
# answer= (int(s) % 10) + 1
# 자릿수 구하려면 그냥 len() 하면 됨.....
print(len(s))

#메모리 초과 터져서
#GPT 가 알려준 대로 쓰면
ans=0
digit=1
start=1
while start <= N:
    end =min(N, start * 10 -1)
    ans += (end - start +1) * digit
    start *= 10
    digit +=1
print(ans)