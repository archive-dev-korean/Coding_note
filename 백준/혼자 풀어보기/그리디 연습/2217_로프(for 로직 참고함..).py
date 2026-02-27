# 그리디 연습
N=int(input())
l=[]
result=[]
for _ in range(N):
    i=int(input())
    l.append(i)
l.sort()
# print(l[0]*N)

# print(l)
#핵심 아이디어 로프를 내림차순으로 정렬후 i,i+1 곱해보기 -> GPT
# for i in range(1,N+1):
#     print(l[0]*i)
# print(l[0]*N)
# print(l)
for i in range(N):
    result.append(l[i]*(N-i))
    # N-=1
# result.sort(reverse=True)
# print(result[0])
print(max(result))
