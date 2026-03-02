# # 연습
x,y=map(int,input().split())
# if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
#     if y%7==0:
#         print('SUN')
#     elif y%7==1:
#         print('MON')
#     elif y%7==2:
#         print('TUE')
#     elif y%7==3:
#         print('WED')
#     elif y%7==4:
#         print('THU')
#     elif y%7==5:
#         print('FRI')
#     else:
#         print('SAT')
#     # y+=3
# elif x==4 or x==6 or x==9 or x==11:
#     if y%7==0:
#         print('SUN')
#     elif y%7==1:
#         print('MON')
#     elif y%7==2:
#         print('TUE')
#     elif y%7==3:
#         print('WED')
#     elif y%7==4:
#         print('THU')
#     elif y%7==5:
#         print('FRI')
#     else:
#         print('SAT')
# else:
#     if y%7==0:
#         print('SUN')
#     elif y%7==1:
#         print('MON')
#     elif y%7==2:
#         print('TUE')
#     elif y%7==3:
#         print('WED')
#     elif y%7==4:
#         print('THU')
#     elif y%7==5:
#         print('FRI')
#     else:
#         print('SAT')

# 이건 28,30,31일 인 달마다 다음달 요일 계산이 안됨
end_of_month=[31,28,31,30,31,30,31,31,30,31,30,31]
week=['MON','TUE','WED','THU','FRI','SAT','SUN']

total=0 # 모든 날짜의 합
for i in range(x-1):
    total+=end_of_month[i]
total+=(y-1) #이거 좀 신기하네 ㅋㅋ -> 며칠이 지났는지 정확히 세기 위한 보정
print(week[total%7])