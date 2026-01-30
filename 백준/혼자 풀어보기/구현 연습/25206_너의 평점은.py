# 구현 연습
d={'A+': 4.5, 'A0':4.0 ,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0.0}
# print(d.items())
ex=[]
ans=0
total=0
# result=[]
for _ in range(20):
    a= input().split()
    ex.append(a)

    #이거 뺴먹음 'P' 받을 때
    # if a[2] =='P':
    #     continue
# print(ex)
for x in ex:
    for y in x:
        if y in d:
           ans+= float(x[1])*d[x[2]]
           total+=float(x[1]) #<- 이런 부분 좀 보고 학습 하면 될 것 같음
        elif y=='P':
            continue
# print(result)
print(round(ans/total,6))