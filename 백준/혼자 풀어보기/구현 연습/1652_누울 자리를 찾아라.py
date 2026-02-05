# 구현 연습
N=int(input())
a=[]
cnt1=0
cnt2=0
for _ in range(N):
    i=input()
    a.append(i)
# print(a)
# for j in a:
#     for k in range(len(j)-1):
#         # print(k)
#         if j[k+1] =='.' and j[k] =='.':
#             cnt1+=1
# for col in range(len(a[0])): # 열
#     for row in range(len(a)-1):
#         if a[row][col] == '.' and a[row+1][col] =='.':
#             # j+=1
#             cnt2+=1
# print(f"{cnt1} {cnt2}")

# 이렇게 짜면 ....는 3개로 계산함 연속한 수 계산함

# 가로 검사
for row in range(N):
    run=0
    for col in range(N):
        if a[row][col] =='.':
            run+=1
        else:
            if run >=2:
                cnt1+=1
            run=0
    if run >=2: # 줄 끝처리
        cnt1+=1
for col in range(N): #세로 검사
    run=0
    for row in range(N):
        if a[row][col] =='.':
            run+=1
        else:
            if run >= 2:
                cnt2 +=1
            run =0
    if run >=2: # 끝처리
        cnt2 +=1
print(cnt1,cnt2)