#해시 연습
N = int(input())
d=dict()
# for _ in range(N):
#     i=input()
#     if i in d:
#         d[i] += 1
#     else:
#         d[i] =1
# # print(d.items())
# G=list(d.items())
# print(G)
# if G.keys() == 'Enter':

#다시 풀기 dictionary 활용
ans=0
for _ in range(N):
    name = input()

    if name == 'ENTER':
        ans += len(d)
        d.clear()
    else:
        d[name] = 1
ans += len(d)
print(ans)

#set 활용해서 다시 풀기
# s=set()
# ans=0
# for _ in range(N):
#     name=input()
#     if name=='ENTER':
#         ans+=len(d)
#         d.clear
#     else:
#         s.add(name)
# ans +=len(d)
# print(ans)

#clear() 안쓰고 풀기
# 1.플래그 Enter 이후부터 세자 라는 방법
ans=0
active=True
for _ in range(N):
    name = input()
    if name =='ENTER':
        ans += len(d)
        d=dict() #여기서 초기화 clear안하고 해줘야 함
        active=True
    elif active: #active가 True면
        d[name] =1 
ans += len(d)
print(ans)

#2. 이 문제에서는 위에서 flag 빼고 해도 정담입 그냥 active 부분만 빼주면 됨