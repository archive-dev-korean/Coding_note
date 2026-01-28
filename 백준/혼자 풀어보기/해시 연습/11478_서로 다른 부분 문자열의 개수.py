#해시 연습

# S=input()
# temp=dict()
# for i in range(len(S)):
#     for j in range(i+1, len(S) + 1):
#         sub=S[i:j]
#         if sub in temp:
#             temp[sub] += 1
#         else:
#             temp[sub] = 1
    
# print(len(temp)) #-> 여기원래 count 써서 value가 1인 값들만 출력하게 했는데 그건 당연히 틀리고
# len() 으로 부분 문자열의 개수만 구하면 되는 거였음


# set() 으로 푸는게 맞음 원래 의도는
S = input()
subs = set()

for i in range(len(S)):
    for j in range(i+1, len(S)+1):
        subs.add(S[i:j])

print(len(subs))
