--문제 : 이 서비스에서는 공간을 둘 이상 등록한 사람을 "헤비 유저"라고 부릅니다. 헤비 유저가 등록한 공간의 정보를 아이디 순으로 조회하는 SQL문을 작성해주세요.
--츨처 : https://school.programmers.co.kr/learn/courses/30/lessons/77487

--두가지 풀이 존재

--오답 :
 SELECT ID, NAME, HOST_ID
 from PLACES 
 group by 3
 having count(HOST_ID) >=2
 order by 1

--이러면 중복 처리된 값이 나와서 원하는 결과 보여주기 어려움 결국 서브 쿼리 사용이 되어야 한다.

--정답 1(서브쿼리 & in 절 활용) :
 SELECT ID, NAME, HOST_ID
 from PLACES 
 WHERE HOST_ID IN (
 SELECT HOST_ID
 FROM PLACES
 GROUP BY HOST_ID
 HAVING COUNT(*) >=2)
# order by 1

--서브 쿼리 안에 둘 이상 등록한 사람 조건에 되어 있고 바깥에 host_id 가 그 조건에 부합하면 결과 값 출력


--정답 2(join 활용) : 
SELECT P.ID, P.NAME, P.HOST_ID
FROM PLACES P
JOIN (
SELECT HOST_ID
FROM PLACES
GROUP BY HOST_ID
    HAVING COUNT(*) >= 2
) H ON P.HOST_ID = H.HOST_ID
ORDER BY 1

-- 결국 같은 말을 다르게 풀어서 쓴 거지만 동일한 데이터를 join을 활용해 원하는 결과값 출력
