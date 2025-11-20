# 출처 : https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 내가 생각한 풀이
# 조합을 만들어서 거기서 중복을 제거하고 세면 된다
import itertools

def solution(nums):
    combos = itertools.combinations(nums, len(nums)//2)
    max_count = 0

    for comb in combos:
        # 조합 내 중복 제거한 종류 수
        count = len(set(comb))
        max_count = max(max_count, count)

    return max_count

# 뭐 맞을 것이다 그러나 시간 복잡도가 상승하게 되어서 찾아보니 

# 단 3줄이면풀 수 있다

def solution(nums):
    # 선택 가능한 최대 마리 수
    max_pick = len(nums) // 2
    
    # 실제 포켓몬 종류 수
    type_count = len(set(nums))
    
    # 답은 둘 중 작은 값
    return min(max_pick, type_count)
