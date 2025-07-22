# 문제 : 이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120885

# 일단 내장함수 안쓰고 10진수를 2진수로 변환하는 로직을 직접 짰고, 10진수에서 다시 2진수로 변환 하는 것은 내장함수 썼다.
def solution(bin1, bin2):
    answer = ''
    t = 1
    sa = 0
    sb = 0
    for i in range(len(bin1) -1,-1,-1):
        if bin1[i] == '1':
            sb +=t
        t *=2
    t=1
    for j in range(len(bin2) -1,-1,-1):
        if bin2[j] == '1':
            sa +=t
        t *=2
    total = sa + sb
    # print(total)
    
    return bin(total)[2:]

# 근데 이렇게 내장함수 1개만 쓸거면 애초에 반쪽짜리 답이라고 생각함. 그래서 처음부터 모두 내장함수 쓰면 간결하게 작성가능함

def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

# 만약 10진수를 다시 2진수로 바꾸고 싶은데 내장함수 안쓰고 로직으로만 구하면 이렇게 쓰면 된다.
def solution(bin1, bin2):
    answer = ''
    t = 1
    sa = 0
    sb = 0
    for i in range(len(bin1) -1,-1,-1):
        if bin1[i] == '1':
            sb +=t
        t *=2
    t=1
    for j in range(len(bin2) -1,-1,-1):
        if bin2[j] == '1':
            sa +=t
        t *=2
    total = sa + sb
    if total == 0:
            return "0"
        
        answer = ''
        while total > 0:
            answer = str(total % 2) + answer
            total //= 2

    return answer

# 하지만 내장함수의 사용법을 알아두는게 훨씬 유리할 것 이다. 나중에 쓸때도 도움이 되고 
