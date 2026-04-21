#일단 처음에 hash라길래 dict로 풀리겠구나 했는데?
#그래서 처음에 key,value 지정해볼까? 고민하다가 많이 해메었음
#그런데 그렇게 풀면 안되었고 결국 set을 쓰는건데
# 그러면 hash가 아니지 않나? 라고 생각함
# 근데 set자체가 hash를 통해 값의 위치를 저장하는 방식
# 그리고 핵심은 일단 구현자체도 좀 이상했고 아이디어도 떠오르지 않았음
# 처음에 lambda써서 나눠야 하나? 이렇게 생각도 했었고

#GPT도움 받아서 풀었는데 보면 이해가 가지만 구현하기에는 좀 힘들었을 것 같음
def solution(phone_book):
    # dict=[]
    answer = True
    # for i in range(len(phone_book)):
    # for i in phone_book:
    #     x=lambda[i:i[:2]]
    #     for j in range(len(i)):
    #        # print(i[j])
    #         if i[j] in phone_book[i]
    phone_set=set(phone_book)
    for i in phone_book:
        print('i',i)
        num=""
        for j in i:
            print('j',j)
            num+=j
            print("num",num)
            if num in phone_set and num !=i:
                print("phone_set",phone_set)
                answer=False
                return answer
    return answer

# 잘라가며 비교 해봐야 함
# 아직 개념이 좀 부족한가... 해시는 = key-value 기반인줄 알았는데 그건 아니었네
# set도 해시 구조임 -> set쓰는 이유는 빠른 조회를 위함임, value기반 해시 = set
# hash : 데이터를 해시 함수로 변환해서 빠르게 찾는 구조
# set에서 저장할 때 hash(value) 위치 계산해서 저장함