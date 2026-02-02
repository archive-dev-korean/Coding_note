# 연습
# S=list(input())
S=input()
# d=dict()
a=[]
# d={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0
d=dict()
alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in alpha:
    d[i] = -1 #-1로 처음부터 저장 해놓으면 편함.
# print(d)
a.extend(S)
# print(a)
for j,v in enumerate(a):
    if v in d and d[v] == -1: #처음 나올때면
        d[v] = j
        # print(d[v])
        # continu

# print(*d.values())
for v in d.values():
    print(v,end=' ')

# 제일 깔끔하게 하면
d = {c:-1 for c in 'abcdefghijklmnopqrstuvwxyz'}

for i,j in enumerate(S):
    if d[i] == -1:
        d[i] = i