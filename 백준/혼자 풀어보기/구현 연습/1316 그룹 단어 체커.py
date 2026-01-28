# 구현 연습
N=int(input())
l=[]
for _ in range(N):
    i= input()
    l.append(i)
# print(l)
# 여기서 부터 핵심
cnt=0
for j in l:
    seen=[]
    group=True

    for k in range(len(j)):
        if j[k] not in seen:
            seen.append(j[k])
            # cnt+=1
        else:
            if j[k] != j[k-1]:
                group = False
                break
    if group: #group 이 True이면
        cnt+=1
print(cnt)