# 그리디 연습
N=int(input())
l=[]
for _ in range(N):
    i=int(input())
    l.append(i)
l.sort(reverse=True)
# print(l[0]*N)

print(l)
#핵심 아이디어 로프를 내림차순으로 정렬후 i,i+1 곱해보기