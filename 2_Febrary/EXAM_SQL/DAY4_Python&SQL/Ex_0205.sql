# =========== <7장 데이터 생성, 조작과 변환> 연속 ============

# 7.3 시간 데이터 처리
# [ cast( ) ]
# - 날짜 데이터를 다른 형식으로 변환
# - cast( 컬럼명 as 데이터형식 )

SELECT cast('2019-09-17	15:30:00' as datetime) as datetime;

# [ str_to_date( ) ]
# 얘도 형변환 함수
# %M : 월이름  %m : 숫자 월 %d: 숫자 일  %Y 연도 4자리 
SELECT str_to_date('September	17,	2019',	'%M	%d,	%Y')	as return_date;

# [ current_date/time/timestamp() ]
# 각 현재 날짜, 현재 시간, 날짜+시간 반환
SELECT CURRENT_DATE(),	CURRENT_TIME(),	CURRENT_TIMESTAMP();

# [ date_add( ) ]

SELECT date_add(current_date(),	interval 5 day);


SELECT last_day('2022-08-01');


SELECT dayname('2022-08-01');


# =============== < 8장. 그룹화와 집계 > ================
# [ group by ]
# : 특정 컬럼의 데이터를 그룹화
# 	집계 함수 사용
use sakila;


# [ Indexing ]
# : 그룹화하면 인덱싱 가능; order by 2

SELECT customer_id,	count(*)
FROM rental
GROUP	BY customer_id
ORDER	BY 2 desc;

# [ having ]
# : group by 후에는 where이 아닌 having 사용

SELECT customer_id,	count(*)
FROM rental
# where count(*) >= 40
GROUP	BY customer_id
having count(customer_id) >= 40
ORDER	BY 2 desc;


# [ 집계 함수 ] --- max() min() avg() sum() count() ---
desc payment ; 
# 타입 확인
# - decimal(5,2): (전체 자리수(소수 포함), 소수 자리수)

# 집계 함수 사용: select절에 사용할 수 있다

SELECT max(amount)	as max_amt,
	min(amount)	as min_amt,
	avg(amount)	as avg_amt,
	sum(amount)	as tot_amt,
	count(*)	as num_payments
FROM payment;  # 전체 칼럼을 그룹으로 보고 연산

# 그룹화하지 않으면 오류 발생:
#  다른 칼럼이 없으면 전체를 그룹으로 보고 연산,
#  특정 칼럼이 있으면 오류 발생
SELECT customer_id ,
	min(amount)	as min_amt,
	avg(amount)	as avg_amt,
	sum(amount)	as tot_amt,
	count(*)	as num_payments
FROM payment;

# 특정 칼럼 그룹화:
#  해당 칼럼 그룹별 연산 값을 출력
SELECT customer_id ,
	min(amount)	as min_amt,
	avg(amount)	as avg_amt,
	sum(amount)	as tot_amt,
	count(*)	as num_payments
FROM payment
group by customer_id ;


# 그냥 count() : 중복 포함
# distinct	 : 중복 미포함
SELECT count(customer_id)	as num_rows,
count(distinct customer_id)	as num_customers
FROM payment;


# 표현식 사용
# - 


# null: 함수들은 무시한다
use sqlclass_sb;
CREATE TABLE number_tbl (val smallint);
desc number_tbl;

INSERT	INTO number_tbl VALUES(1);
INSERT	INTO number_tbl VALUES(3);
INSERT	INTO number_tbl VALUES(5);

SELECT count(*)	as num_rows,
	count(val)	as num_vals,
	sum(val)	as total,
	max(val)	as max_val,
	avg(val)	as avg_val
FROM number_tbl; # 3 3 9 5 3

INSERT	INTO number_tbl VALUES (NULL);

SELECT count(*)	as num_rows,
	count(val)	as num_vals,
	sum(val)	as total,
	max(val)	as max_val,
	avg(val)	as avg_val
FROM number_tbl; # 4 3 9 5 3
# count()는 증가하지만
# 나머지 함수에선 null 반영하지 않음


# ------------------ [그룹 생성] ----------------------
# [ 단일 열 그룹화 ]
# - 한 열을 그룹화 -> count() 사용 가능
use sakila;
SELECT actor_id, count(*)
FROM film_actor
GROUP BY actor_id;


# [ 다중 열 그룹화 ]
# 그룹화를 여러 번 하는 것
#  첫 번째 칼럼: 그룹화 (인덱싱)
#  두 번째 칼럼: 집계 - 연산

SELECT fa.actor_id,	f.rating, count(*)
FROM film_actor as fa
	INNER JOIN film as f
	on fa.film_id =	f.film_id
GROUP BY fa.actor_id, f.rating
ORDER BY 1, 2; # order by로 첫 열 정렬 설정


# [ with rollup ] 롤업 생성
# : 각 그룹별 상단에 합계를 추가하는 함수

SELECT fa.actor_id,	f.rating,	count(*)
FROM film_actor as fa
	inner join film	as f
	on fa.film_id =	f.film_id
GROUP BY fa.actor_id, f.rating with rollup
ORDER by 1, 2; # 1 null 19
# 결과: 1번 인덱스	null	sum(group1)


# -------------- [ 그룹 필터 ] ----------------
# [ where having ]
# : 둘 다 사용 가능

SELECT fa.actor_id,	f.rating, count(*)
FROM film_actor fa
	INNER JOIN film	f
	ON fa.film_id =	f.film_id
WHERE f.rating in ('G','PG')
GROUP BY fa.actor_id, f.rating
HAVING count(*)	> 9;
# group by로 생긴 count()를 where에 못 보내는거지
# where을 못 쓰는 건 아니다

# 실습:
SELECT customer_id,	count(*), sum(amount)
FROM payment
GROUP	BY customer_id;

# FIN.