문제 : 정수 배열 array와 정수 n이 매개변수로 주어질 때, array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.
출처 : https://school.programmers.co.kr/learn/courses/30/lessons/120890

일단 리스트를 정렬해서 가장 배열의 값에서 n을 뺸 값을 절댓값을 씌워서 가장 작은 걸 구하면 된다고 생각함

이걸 구현하는게 문제인데
처음 시도한것은 
def solution(array, n):
    answer = 0
    for i in array:
        ab=abs(i - n)
        answer=ab.sort()
    return answer[0]
  이렇게 시도 했는데 타입이 맞지 않아서 에러남

람다식을 쓰면 간단히 해결가능할 것 같고 가까운 수를 구하는 것은 먼저 오름차순으로 정렬하면 됨
def solution(array,n):
    array.sort()
    return min(array, key=lambda x: abs(x-n))

이렇게 하............. 아이디어만 생각하면 뭐하냐고 .....
