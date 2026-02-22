# 구현 연습
N,M=map(int,input().split())
s=[]
for _ in range(N):
    i=input()
    s.append(i)
DNA=['A','C','G','T']
result=""
cnt=0
# s=[0] * M
# # for _ in range(M):
# #     for i in DNA:
# #         s.append(i)
# # # s=[0] * M
# if s[0]=='A':
#     for j in i:
#         j!=s[0]
# print(s)

# 이거는 각 열에서 가장 많은 문자를 세서 그게 s로 최종나와야 함
# 여기까지 GPT 아이디어 참고함
for i in range(M):
    count=[0,0,0,0] # A,C,G,T의 개수
    for j in range(N):
        if s[j][i] == "A":
            count[0] +=1
        elif s[j][i] =="C":
            count[1] +=1
        elif s[j][i] =="G":
            count[2] +=1
        elif s[j][i] =="T":
            count[3] +=1
    maxcnt=count.index(max(count))
    result+=DNA[maxcnt]

    cnt+=N-max(count)
print(result)
print(cnt)
