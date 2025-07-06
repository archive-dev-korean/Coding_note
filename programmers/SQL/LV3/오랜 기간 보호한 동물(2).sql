--문제 : 입양을 간 동물 중, 보호 기간이 가장 길었던 동물 두 마리의 아이디와 이름을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 기간이 긴 순으로 조회해야 합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59411

--오답 1(서브 쿼리 활용) : 
SELECT i.ANIMAL_ID, i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where o.DATETIME - i.DATETIME in (
select max(datediff(o.DATETIME , i.DATETIME))
from ANIMAL_INS i join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
group by i.ANIMAL_ID
order by 1 desc)
limit 2

--내 생각에서 논리적으로 오류는 없어 보이지만 조금 테스트 결과는 정답과 다른 값이 출력됨

--오답 2(일반 조건 절과 그룹바이 절): 
SELECT i.ANIMAL_ID, i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where i.DATETIME - o.DATETIME 
group by 1
order by (i.DATETIME - o.DATETIME)  desc
limit 2
--order by 절에서 datetime 연산을 잘못함 그래서 다른 결과가 출력됨

--정답 : 
SELECT i.ANIMAL_ID, i.NAME
from ANIMAL_INS i join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
order by (o.DATETIME - i.DATETIME)  desc
limit 2

--불필요한 절 제거하고 가장 깔끔하게 작성한 쿼리 



-- 이 문제에서 datediff 사용해서 풀수도 있지만 문제 조건에서 일 수 기준으로 비교하란 조건이 없었기 때문에 굳이 사용할 필요 없이 date 끼리 연산해도 정답으로 인정됨
