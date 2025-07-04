--문제 : 대장균 개체의 ID(ID)와 자식의 수(CHILD_COUNT)를 출력하는 SQL 문을 작성해주세요. 자식이 없다면 자식의 수는 0으로 출력해주세요. 이때 결과는 개체의 ID 에 대해 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/299305

--오답 쿼리 : 
 select p.ID, count(c.ID) as CHILD_COUNT
 from ECOLI_DATA p join ECOLI_DATA c
 on p.PARENT_ID = c.ID
 where c.ID = c.PARENT_ID
 group by c.ID
 order by 1

--inner join을 해버려서 올바른 데이터가 null처리 된 데이터가 잘 조인되어지지 않았다 그래서 outer join을 사용해 다시 조인해야 한다

--정답 쿼리 : 
SELECT e.ID,
       COUNT(c.ID) AS CHILD_COUNT
FROM ECOLI_DATA e
LEFT JOIN ECOLI_DATA c
    ON e.ID = c.PARENT_ID
GROUP BY e.ID
ORDER BY e.ID ASC;

--join 사용법을 다시 한번 알아둘 필요가 있을 것 같다.
