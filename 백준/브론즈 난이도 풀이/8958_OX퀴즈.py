# 연습
N=int(input())
# d=dict()
for _ in range(N):
    Quiz=list(input())
    cnt=0
    d={"score":0}
    # print(Quiz)
    for j in Quiz:
        if j=='O':
            cnt+=1
            # d[score]+=cnt
            d['score'] +=cnt
                # print(d)
        else:
            cnt=0
            # print(d)
    # print(d.values())
    for i in d.values():
        print(i)
# 딕셔너리 써도 되지만
N = int(input())

for _ in range(N):
    quiz = input().strip()
    cnt = 0
    score = 0

    for ch in quiz:
        if ch == 'O':
            cnt += 1
            score += cnt
        else:
            cnt = 0

    print(score)
# 이렇게 쓰면 똑같은 기능 쓰는거잖아?