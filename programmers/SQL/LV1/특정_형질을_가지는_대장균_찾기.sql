--문제: 2번 형질이 보유하지 않으면서 1번이나 3번 형질을 보유하고 있는 대장균 개체의 수(COUNT)를 출력하는 SQL 문을 작성해주세요. 1번과 3번 형질을 모두 보유하고 있는 경우도 1번이나 3번 형질을 보유하고 있는 경우에 포함합니다.
-- 출처: 프로그래머스 Lv1 (https://school.programmers.co.kr/learn/courses/30/lessons/301646)

-- 비트 연산자 활용
select 
count(*) as COUNT
from ECOLI_DATA
where GENOTYPE & 2 = 0 and (GENOTYPE & 1 > 0 or GENOTYPE & 4 > 0)
