# 연습
# from collections import deque
# d=deque()
N=int(input())
l=[]
result=[]
for _ in range(N):
    t=input()
    l.append(t)
# print(l)
# for i in range(N):
#     if l[i]=="KBS1":
#         if i > 0:

# 이건 좀 어려운데(체감)
# 그래서 어떻게 푸는지 참고함
cur=0 # 커서 위치
pos1 = l.index("KBS1")
# print(pos1)
while cur<pos1: # 커서를 pos1 까지 내리기 (버튼1)
    result.append(1)
    cur+=1
while cur>0: #KBS1을 맨 위로 올리기(버튼4)
    result.append(4)
    l[cur],l[cur-1]=l[cur-1],l[cur]
    cur-=1
pos2 = l.index('KBS2') # 여기서 초기화 해줘야 됨 (위치가 바뀌었기 때문)
while cur < pos2:
    result.append(1)
    cur+=1
while cur>1: #KBS2를 1번으로 올리기(cur을 1까지)
    result.append(4)
    l[cur],l[cur-1] = l[cur-1],l[cur]
    cur-=1
print(*result,sep='')
