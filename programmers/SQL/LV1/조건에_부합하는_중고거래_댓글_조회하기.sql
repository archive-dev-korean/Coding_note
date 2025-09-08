--문제: USED_GOODS_BOARD와 USED_GOODS_REPLY 테이블에서 2022년 10월에 작성된 게시글 제목, 게시글 ID, 댓글 ID, 댓글 작성자 ID, 댓글 내용, 댓글 작성일을 조회하는 SQL문을 작성해주세요. 결과는 댓글 작성일을 기준으로 오름차순 정렬해주시고, 댓글 작성일이 같다면 게시글 제목을 기준으로 오름차순 정렬해주세요.
--출처: https://school.programmers.co.kr/learn/courses/30/lessons/164673

--오답1
select  b.TITLE,
     b.BOARD_ID,
     r.REPLY_ID,
     r.WRITER_ID,
     r.CONTENTS,
     Date_format(r.CREATED_DATE, "%Y-%m-%d") as CREATED_DATE
 from USED_GOODS_BOARD b, USED_GOODS_REPLY r
 where b.BOARD_ID = r.BOARD_ID and Date_format(r.CREATED_DATE, "%Y-%m") = '2022-10'
 order by r.CREATED_DATE asc, b.TITLE asc
-- 쿼리 결과는 똑같지만 where조건에서 ='2022-10'조건으로 적어서 오답으로 인식함

--정답
select  b.TITLE,
    b.BOARD_ID,
    r.REPLY_ID,
    r.WRITER_ID,
    r.CONTENTS,
    Date_format(r.CREATED_DATE, "%Y-%m-%d") as CREATED_DATE
from USED_GOODS_BOARD b, USED_GOODS_REPLY r
where b.BOARD_ID = r.BOARD_ID and b.CREATED_DATE between '2022-10-01' and '2022-10-31'
order by r.CREATED_DATE asc, b.TITLE asc
-- between 조건으로 변경하면 정답처리 


-- 조금더 명확하게 하자면
SELECT 
     b.TITLE,
     b.BOARD_ID,
     r.REPLY_ID,
     r.WRITER_ID,
     r.CONTENTS,
     DATE_FORMAT(b.CREATED_DATE, '%Y-%m-%d') AS CREATED_DATE
 FROM 
     USED_GOODS_BOARD b
 JOIN 
     USED_GOODS_REPLY r
 ON 
     b.CREATED_DATE = r.CREATED_DATE
WHERE b.CREATED_DATE BETWEEN '2022-10-01' AND '2022-10-31'
ORDER BY 
     b.CREATED_DATE, b.TITLE ASC
-- 이렇게 적는게 나음(가독성)

