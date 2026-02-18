# 구현 연습
w=input()
# print(len(w))
first=[]
second=[]
third=[]
cand=[]
# 3등분으로 나누는 부분인데 여기서 슬라이싱 범위 개념 쓰면 알아서 1개이상의 수로 나뉘어짐 이게 핵심
for i in range(1,len(w)-1):
    for j in range(i+1,len(w)):
        first=w[:i]
        second=w[i:j]
        third=w[j:]
    cand.append(first[::-1]+second[::-1]+third[::-1])
print(min(cand))
# 슬라이싱[포함:미포함] [a:b] -> a이상 b미만