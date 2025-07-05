--문제 : USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 완료된 중고 거래의 총금액이 70만 원 이상인 사람의 회원 ID, 닉네임, 총거래금액을 조회하는 SQL문을 작성해주세요. 결과는 총거래금액을 기준으로 오름차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/164668

--정답 : 
SELECT u.USER_ID, u.NICKNAME, sum(b.price) as TOTAL_SALES
from USED_GOODS_BOARD b join USED_GOODS_USER u on b.WRITER_ID = u.USER_ID
where b.STATUS = 'DONE' 
group by 1
having sum(b.price) >= 700000
order by 3

--서브쿼리와 조인 사용해서 하는 것보다 group by 써서 적는게 조금더 간편한 것 같다.
