# 그리디 연습
# math=map(input().split('-','+'))
# math=input()
# # text=['+','-','(',')']
# for i in math:
#     if i=='-' or i=='+':
#         continue

# print(math)


# 최적해 구하는 것 -> "-" 로 구분된 수만 파악해서 이후의 수만 전부 뺴면 됨***
# 이게 핵심 아이 디어 임 +,- 섞여 있어도 똑같이 해당됨 -만 나와도 똑같음
math=input().split('-')
result=0
# print(math)
# # first=math[0].split('+')
# # result+=sum
# for i in math:
# result+=int(math[0])
# for i in range(math):
#     result-=int


# 첫번쨰 는 더하기
# first=math[0].split('+')
# result+=sum(map(int,first))

# #나머지는 전부 뺴기
# for i in math[1:]:
#     nums=i.split('+')
#     result-=sum(map(int,nums))
# print(result)

# 약간 조금 더 직관적
for i in range(len(math)):
    numbers=math[i].split('+')
    sum=0
    for j in numbers:
        sum+=int(j)

    if i==0:
        result+=sum
    else:
        result-=sum
print(result)