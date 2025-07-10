# 문제 : 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.

def solution(n):
    sum=0
    for i in range(n+1):
        if i%2 == 0:
           sum += i
        else:
            pass
    return sum

# 헷갈렸던 부분 :  당시 문제를 풀때는 언어에 익숙하지 않았던 것 같다. sum ++ 라고 썼었다.
