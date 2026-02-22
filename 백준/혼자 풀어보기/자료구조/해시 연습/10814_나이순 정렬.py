# 해시 연습
# N = int(input())
# d=dict()
# for i in range(N):
#     a,name= input().split()
#     a= int(a)
#     if name in d:
#         d[name] += a    
#     else:   
#         d[name] = a
# # for k,v in sorted(d.values()):
# #            print(v,k)
# for k,v in sorted(d.items(), key=lambda x: x[1]):
#     print(v,k)
# print(d.items())
# print(d.values

#주의 점 : 입력 형태
#주의 점 : 딕셔너리 정렬 형태

#위에 코드는 틀렸음 다시 풀어보면
N= int(input())
d = dict()
for i in range(N):
    age, name = input().split()
    age = int(age)
    if age in d:
        d[age].append(name) # 21 : {'junkyu','Dohyun'} 이런식으로 저장됨
    else:
        d[age] = [name] #<- 여기서 name으로 적으면 틀림 왜냐면 처음엔 str 쓰다가 if 마주치면 갑자기 append하니까 타입에 안맞음 따라서 처음부터 list 써주는게 맞음
for age in sorted(d.keys()):
    for name in d[age]:
        print(age,name)