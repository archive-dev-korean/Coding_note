--문제 : 3세대의 대장균의 ID(ID) 를 출력하는 SQL 문을 작성해주세요. 이때 결과는 대장균의 ID 에 대해 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/301650

--정답 1(계층 쿼리 사용, 가장 추천) : 
with RECURSIVE cnt as (
select ID, PARENT_ID, 1 as level
from ECOLI_DATA 
where PARENT_ID is null

union all 

select e.ID, e.PARENT_ID, c.level + 1
from ECOLI_DATA e join cnt c on e.PARENT_ID = c.ID
)
select ID 
from cnt
where level = 3
order by 1 asc

--계층 쿼리는 oracle 일 떄만 알고 어떻게 사용하는지 알고 있었는데 이번 문제를 풀면서 mysql에서도 어떻게 사용하는지 알게됨
--가장 헷갈리는 점은 부모 자식간에 연결이 조금 헷갈림
--처음엔 c.PARENT_ID = e.ID 이렇게 연결 했었음 이러면 순서가 역방향이 됨. 연결 부분에서 어떻게 연결해야 순방향이고, 역방향인지 알아둘 필요가 있을 것 같음.
--또한 with recursive 문도 공부해봐야 겠음

--정답 2(다중 join 활용, 비추천) :
select d3.ID 
from ECOLI_DATA d1 join ECOLI_DATA d2 on d1.ID = d2.PARENT_ID
join ECOLI_DATA d3 on d2.ID = d3.PARENT_ID
where d1.PARENT_ID is null
order by 1

--직접 일일히 세대를 찾아가며 부모의 ID와 자식의 ID가 일치하는지 알아보면서 도출하는 방식임
--문제에서 운좋게 3세대 이렇게 나와서 그나마 간단해 보이지만 실전에서 방대한 데이터에서 100세대 이런식으로 나와 버리면 못 품. 
--따라서 계층 쿼리가 필수적으로 필요해 보임
