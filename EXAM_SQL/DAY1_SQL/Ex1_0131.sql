use testdb;

create table person 
	(person_id smallint unsigned,
	fname VARCHAR(20),
	lname VARCHAR(20),
	eye_clor ENUM('BR', 'BL', 'GR'),
	birth_date DATE,
	street VARCHAR(30),
	city VARCHAR(20),
	state VARCHAR(20),
	country VARCHAR(20),
	postal_code VARCHAR(20),
	constraint pk_person primary key (person_id)
	);
	
desc person;

create table favorite_food
	(person_id smallint unsigned,
	food VARCHAR(20),
	constraint pk_favorite_food primary key (person_id, food),
	constraint fk_fav_food_person_id foreign key (person_id) references person(person_id)
	);


# [ alter ] 테이블 수정 ---------------------
set foreign_key_checks=0; # 비활성화
alter table person modify person_id smallint unsigned auto_increment;  # auto_increment: 숫자 자동 추가
set foreign_key_checks=1; # 활성화


# [Insert ] 데이터 추가 ----------------------
insert into person
	(person_id, fname, lname, eye_clor, birth_date)
	values (null, 'William', 'Turner', 'BR', '1972-05-27');


# [ select ] 데이터 확인
select * from person;


# 특정 필드 기준 검색
select person_id, fname, lname, birth_date from person;


# [ where ] 특정 조건을 정하여 검색
select person_id, fname, lname, birth_date from person
where lname='Turner';


# 데이터 추가 연습 2 ( insert into )
insert into favorite_food (person_id, food)
values (1, 'pizza');

insert into favorite_food (person_id, food)
values (1, 'cookies');

insert into favorite_food (person_id, food)
values (1, 'nachos');

select * from favorite_food;

# 한 번에 여러 행 추가 ----------------------
delete from favorite_food where person_id=1;

select * from favorite_food;

insert into favorite_food (person_id, food)
values (1, 'pizza'), (1, 'cookie'),(1, 'nachos');
# values val1, val2, ...


# [ order by ] 알파벳 순서로 정렬 ------------
select food from favorite_food
where person_id=1 order by food;


# 데이터 추가 ------------------------------
insert into person
(person_id, fname, lname, eye_clor, birth_date, street,city, state , country , postal_code )
values(null, 'Susan', 'Smith', 'BL', '1975-11-02', '23 Maple St.',
'Arlington', 'VA', 'USA', '20220');

select * from person;


# [ Update ] 데이터 수정 -------------------
update person
set street = '1225 Tremon St.',
	city = 'Boston',
	state = 'MA',
	country = 'USA',
	postal_code = '02138'
where person_id = 1;

select * from person;

# [ Delete ] 데이터 삭제 ---------------------
delete from person where person_id=2;

select * from person;


# 오류 구문: 호출한 외래키가 존재하지 않을 때 -----------------------
# insert into favorite_food (person_id, food) values (3, 'lasagna');
# (3, 'lasagna') 의 3번이 없어 오류 발생

# 해결: 데이터 추가 (=3 또는 =null)
insert into person (person_id, fname, lname) values(3, 'Kevin', 'Kern');
# or ... values (null, 'Kevin', ...);
select * from person;

# 이제 가능
insert into favorite_food (person_id, food) values (3, 'lasagna');
select * from favorite_food;
# ------------------------------------------------------

# 오류 구문2
# update person set birth_date = 'DEC-21-1980' where person_id=1;
# Error: Data truncation: Incorrect date value: 'DEC-21-1980' for column 'birth_date' at row 1


# str_to_date( ) : 날짜 변환 함수
update person set birth_date = str_to_date('DEC-21-1980', '%b-%d-%Y')
where person_id =1;

select * from person;
