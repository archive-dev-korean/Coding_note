# 딕셔너리로 풀면 됨
d = dict()
T = int(input())
for i in range(T):
    book = input()
    if book in d: # 기존에 책이 있다면
        d[book] +=1
    else: #새로 들어온 책
        d[book] = 1
# print(d.keys()) # <- key 값만 모아서 반환
# print(d.values()) # <- value만 모아서 반환
# print(d.items()) # <- key,value 모두 모아서 반환
m = max(d.values())
candidate =[]
for k,v in d.items():
    # print(k,v)
    if v == m:
        candidate.append(k)
# candidate.sort()
# print(candidate[0])
# 이렇게 써도 되고
print(sorted(candidate)[0]) #이렇게 써도 됨