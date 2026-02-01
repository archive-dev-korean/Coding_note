# # 구현 연습
# n=int(input())
# a=[]
# for _ in range(n):
#     i=input().split()
#     i[3] =int(i[3])
#     i[2] =int(i[2])
#     i[1] =int(i[1])
#     a.append(i)
# # print(a)
# # ma=[]
# ma1=max(i[3] for i in a)
# ma2=max(i[2] for i in a)
# ma3=max(i[1] for i in a)

# mia1=min(i[3] for i in a)
# mia2=min(i[2] for i in a)
# mia3=min(i[1] for i in a)
# for i in a:
#     if i[3] == ma1 and i[2]==ma2 and i[1] ==ma3:
#       print(i[0])
# for j in a:
#    if j[3] == mia1 and j[2] ==mia2 and j[1] == mia3:
#       print(j[0])
n=int(input())
a=[]
for _ in range(n):
    name,d,m,y=input().split()
    # d=int(d); m=int(m); y=int(y)
    d=int(d)
    m=int(m)
    y=int(y)
    a.append([name,d,m,y])
print(a)
young=max(a,key=lambda x: (x[3],x[2],x[1]))
old=min(a, key=lambda x:(x[3],x[2],x[1]))

print(young[0])
print(old[0])

# 또는
n = int(input())
a = []
for _ in range(n):
    name, d, m, y = input().split()
    d = int(d); m = int(m); y = int(y)
    a.append([name, d, m, y])

# 초기값: 첫 번째 사람을 기준으로 잡기
young = a[0]  # 가장 어린 사람(생일이 가장 큼)
old = a[0]    # 가장 나이 많은 사람(생일이 가장 작음)

for i in a:
    # i가 더 어리면(생일이 더 늦으면) young 갱신
    if (i[3] > young[3]) or (i[3] == young[3] and i[2] > young[2]) or (i[3] == young[3] and i[2] == young[2] and i[1] > young[1]):
        young = i

    # i가 더 나이 많으면(생일이 더 빠르면) old 갱신
    if (i[3] < old[3]) or (i[3] == old[3] and i[2] < old[2]) or (i[3] == old[3] and i[2] == old[2] and i[1] < old[1]):
        old = i

print(young[0])
print(old[0])
