--문제 : USED_GOODS_BOARD와 USED_GOODS_USER 테이블에서 중고 거래 게시물을 3건 이상 등록한 사용자의 사용자 ID, 닉네임, 전체주소, 전화번호를 조회하는 SQL문을 작성해주세요. 이때, 전체 주소는 시, 도로명 주소, 상세 주소가 함께 출력되도록 해주시고, 전화번호의 경우 xxx-xxxx-xxxx 같은 형태로 하이픈 문자열(-)을 삽입하여 출력해주세요. 결과는 회원 ID를 기준으로 내림차순 정렬해주세요.
--출처 : https://school.programmers.co.kr/learn/courses/30/lessons/164670

SELECT u.USER_ID, u.NICKNAME, concat_ws(' ',u.CITY,u.STREET_ADDRESS1,u.STREET_ADDRESS2) as 전체주소, concat(substring(u.tlno, 1,3), '-', substring(u.tlno, 4,4), '-', substring(u.tlno,8)) as 전화번호
from USED_GOODS_USER u join USED_GOODS_BOARD b
on u.USER_ID = b.WRITER_ID
group by 1
having count(u.USER_ID) >= 3 
order by 1 desc

-- 3건이상 이란 집계 조건이 붙어서 gropu by 하고 having으로 집계 조건줌

--다만 주의 할 점이 concat사용이 익숙치 않아서 사용법 연습이 조금 더 필요할 것 같음
