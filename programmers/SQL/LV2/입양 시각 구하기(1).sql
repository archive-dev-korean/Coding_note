--문제 : 보호소에서는 몇 시에 입양이 가장 활발하게 일어나는지 알아보려 합니다. 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지 조회하는 SQL문을 작성해주세요. 이때 결과는 시간대 순으로 정렬해야 합니다.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/59412

SELECT HOUR(DATETIME) as HOUR, count(*) as COUNT
from ANIMAL_OUTS 
where HOUR(DATETIME) between 9 and 19
group by 1
order by 1 asc

--hour로 시간 추출 해서 그룹별로 카운트 하고 오름차순으로 정렬함
