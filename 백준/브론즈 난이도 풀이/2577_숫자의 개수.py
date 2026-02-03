# 연습
A=int(input())
B=int(input())
C=int(input())
d=dict()
for i in range(10):
    d[i] =0
# print(d)
M=A*B*C
# print(type(M))
for i in str(M):
    if int(i) in d:
        d[int(i)] +=1
# print(*d.values(),end='\n')
for v in d.values():
    print(v)