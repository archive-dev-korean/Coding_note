문제 : 순서쌍이란 두 개의 숫자를 순서를 정하여 짝지어 나타낸 쌍으로 (a, b)로 표기합니다. 자연수 n이 매개변수로 주어질 때 두 숫자의 곱이 n인 자연수 순서쌍의 개수를 return하도록 solution 함수를 완성해주세요.

def solution(n):
    count =0
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a*b == n:
                count+=1
    return count

#이중 for문 사용 

#정석 풀이 
def solution(n):
    count = 0
    for a in range(1, int(n**0.5) + 1):
        if n % a == 0:
            b = n // a
            if a * b == n:
                # (a, b)와 (b, a) → 두 개씩 세기
                if a == b:
                    count += 1
                else:
                    count += 2
    return count
# 순서쌍의 개술 구하는 로직을 생각하지 못했다 처음에는 그래서 어떻게 풀어야 하는지 몰라서 코드 참고했음.
