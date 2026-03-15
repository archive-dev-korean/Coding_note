# 연습
l=[]
for _ in range(5):
    i=int(input())
    l.append(i)
for x in l:
    avg=sum(l)//5
    l.sort()
print(avg)
print(l[2])