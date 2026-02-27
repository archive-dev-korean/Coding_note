# 연습
max_value=0
row=0
col=0
l=[]
for _ in range(9):
    i=list(map(int,input().split()))
    l.append(i)
# print(max(l))
for x in range(9): # 행(몇번째 행)
    # print(max(x))
    for j in range(9): #열 (몇번째 열)
        # print(max(i))
        if l[x][j] > max_value: # 이게 최댓값 구하는 건데 이건 외워 두자 진짜..
            max_value= l[x][j]
            row=x
            col=j
    # if l[]
print(max_value)
print(row+1, col+1)
