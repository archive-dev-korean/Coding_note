--문제 : 동물 보호소에 들어온 동물 중 고양이와 개가 각각 몇 마리인지 조회하는 SQL문을 작성해주세요. 이때 고양이를 개보다 먼저 조회해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59040

SELECT ANIMAL_TYPE, count(*) as count
from ANIMAL_INS 
where ANIMAL_TYPE ='Cat' OR ANIMAL_TYPE ='Dog'
group by 1 
order by 1 asc

--where 절에서 or 말고 in ('Cat','Dog') 써도 됨
