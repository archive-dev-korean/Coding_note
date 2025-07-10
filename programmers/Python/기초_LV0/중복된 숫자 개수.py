# 문제 : 정수가 담긴 배열 array와 정수 n이 매개변수로 주어질 때, array에 n이 몇 개 있는 지를 return 하도록 solution 함수를 완성해보세요.

def solution(array, n):
    return len([i for i in array if i== n])

# 이렇게 풀어도 되고

def solution(array, n):
    return array.count(n)
# 이렇게 풀어도 되고 count()는 내장 메서드 이다.

def solution(array,n):
    count =0
    for i in array:
        if i ==n:
            count += 1
    return count

# 이렇게 풀어도 된다. 가장 정석이다.
