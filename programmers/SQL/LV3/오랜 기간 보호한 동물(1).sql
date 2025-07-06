--문제 : 아직 입양을 못 간 동물 중, 가장 오래 보호소에 있었던 동물 3마리의 이름과 보호 시작일을 조회하는 SQL문을 작성해주세요. 이때 결과는 보호 시작일 순으로 조회해야 합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59044

--정답 1(outer join 활용) : 
SELECT i.NAME, i.DATETIME
from ANIMAL_INS i left outer join ANIMAL_OUTS o on i.ANIMAL_ID = o.ANIMAL_ID
where o.ANIMAL_ID is null
order by 2 asc
limit 3

--정답 2(서브 쿼리 활용) : 
SELECT A.NAME, A.DATETIME
FROM ANIMAL_INS A 
WHERE ANIMAL_ID NOT IN (
    SELECT ANIMAL_ID
    FROM ANIMAL_OUTS
)
ORDER BY A.DATETIME
LIMIT 3

--입양을 가지 않았다면 animal_outs 테이블에 정보 자체가 없을 것이기 때문에 animal_ins 기준으로 outer join 하면 입양을 가지 않은 동물의 값들이 null로 되기 떄문에 그 점을 이용함
--서브 쿼리는 join을 활용하지 않고도 풀 수 있는 방법
--둘다 가독성이 나쁘지 않기 때문에 어느 걸 써도 무방할듯
