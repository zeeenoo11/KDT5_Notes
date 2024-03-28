import pymysql as ps
import pandas as pd
execute_num = 5

# 1.
# 제시된 2개의 테이블을 생성하고, sql 문장을 작성하시오.
if execute_num == 0:
    conn = ps.connect(host='localhost', user='root', password='1234', db='shoppingmall', charset='utf8')
    curs = conn.cursor()

    create_1 = """
    CREATE TABLE user_table(
        userID char(8) not null primary key,
        userName varchar(10) not null,
        birthYear int not null,
        addr char(2) not null,
        mobile1 char(3),
        mobile2 char(8),
        height smallint,
        mDate DATE)"""

    create_2 = """
    CREATE TABLE buy_table(
        num int not null primary key auto_increment,
        userID char(8) not null,
        prodName char(6) not null,
        groupName char(4),
        price int not null,
        amount smallint not null)"""

    insert_t1 = """
    insert into user_table
    values 
        ('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'),
        ('KJD', '김제동', 1974, '경남', NULL, NULL, 173, '2013-03-03'),
        ('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
        ('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-05-05'),
        ('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
        ('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
        ('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
        ('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-05-05'),
        ('SDY', '신동엽', 1971, '경기', NULL, NULL, 176, '2008-10-10'),
        ('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08')"""

    insert_t2 = """
    insert into buy_table
    values
        (1, 'KHD', '운동화', NULL, 30, 2),
        (2, 'KHD', '노트북', '전자', 1000, 1),
        (3, 'KYM', '모니터', '전자', 200, 1),
        (4, 'PSH', '모니터', '전자', 200, 5),
        (5, 'KHD', '청바지', '의류', 50, 3),
        (6, 'PSH', '메모리', '전자', 80, 10),
        (7, 'KJD', '책', '서적', 15, 5),
        (8, 'LHJ', '책', '서적', 15, 2),
        (9, 'LHJ', '청바지', '의류', 50, 1),
        (10, 'PSH', '운동화', NULL, 30, 2),
        (11, 'LHJ', '책', '서적', 15, 1),
        (12, 'PSH', '운동화', NULL, 30, 2)"""

    curs.execute(create_1)
    curs.execute(create_2)
    curs.execute(insert_t1)
    curs.execute(insert_t2)
    conn.commit()   # insert 시 꼭 commit()!
    print('테이블 생성 및 데이터 입력 완료')

    # [INNER JOIN] 확인
    inner_Join = '''
    select * 
    from user_table
        inner join buy_table
        on user_table.userID = buy_table.userID'''

    curs.execute(inner_Join) # 실행
    rows = curs.fetchall()
    df = pd.DataFrame(rows)
    print(df)

    conn.close()

# 2.
# 두 테이블을 내부 조인(buy_table.useID와 user_table.userID)한 다음,
# 아래의 결과와 같이 출력이 되도록 SQL 쿼리를 작성하시오.
# 1) 내부 조인한 결과에 '연락처' 컬럼 추가
if execute_num == 1:
    conn = ps.connect(host='localhost', user='root', password='1234', db='shoppingmall', charset='utf8')
    curs = conn.cursor()
    # sql문 입력
    insert_contact = """
    select userName, prodName, addr,
    concat(
        mobile1, mobile2
        ) as 연락처
    from user_table as ut
        inner join buy_table as bt
        on bt.userID = ut.userID
    """
    # sql문 실행
    curs.execute(insert_contact)

    # 출력
    print('문제 1번')
    print('-'*50,'\nUserName    prodName    addr    연락처\n', '-'*50, sep='')
    # print(f' {desc[0][0]:<8}  {desc[1][0]:<8} ... ')
    rows = curs.fetchall()
    for row in rows:
        print(row)
    # 종료
    conn.close()

# 2) userID가 KYM인 사람이 구매한 물건과 회원 정보 출력
if execute_num == 2:
    conn = ps.connect(host='localhost', user='root', password='1234', db='shoppingmall', charset='utf8')
    curs = conn.cursor()
    #  sql문 입력
    KYM = """
    select ut.userID, userName, prodName, addr,
        concat(mobile1, mobile2) as 연락처
    from user_table as ut
	    inner join buy_table as bt
	    on bt.userID = ut.userID 
    where ut.userID = 'KYM'"""
    # sql문 실행
    curs.execute(KYM)
    # 출력
    print('문제 2번')
    print('-'*50,'\nUserID      UserName    prodName    addr    연락처\n', '-'*50, sep='')
    rows = curs.fetchall()
    for row in rows:
        print(row)
    # 종료
    conn.close()


# 3) 전체 회원이 구매한 목록을 회원 아이디 순으로 정렬
if execute_num == 3:
    conn = ps.connect(host='localhost', user='root', password='1234', db='shoppingmall', charset='utf8')
    curs = conn.cursor()
    # sql 문 입력
    order_ID = """
        select ut.userID, userName, prodName, addr,
            concat(mobile1, mobile2) as 연락처
        from user_table as ut
    	    inner join buy_table as bt
    	    on bt.userID = ut.userID 
        order by ut.userID"""
    #  sql 문 실행
    curs.execute(order_ID)
    #  출력
    print('문제 3번')
    print('-'*50,'\nUserID      UserName    prodName    addr    연락처\n', '-'*50, sep='')
    rows = curs.fetchall()
    for row in rows:
        print(row)
    #  종료
    conn.close()


# 4) 한 번이라도 구매한 기록이 있는 회원 정보를 회원 아이디 순으로 출력 (distinct 사용)
if execute_num == 4:
    conn = ps.connect(host='localhost', user='root', password='1234', db='shoppingmall', charset='utf8')
    curs = conn.cursor()
    #  sql 문 입력
    distinct_ID = """
    select ut.userName, prodName, addr
    from user_table as ut
        inner join buy_table as bt
        on bt.userID = ut.userID
    order by ut.userID"""
    # sql 문 실행
    curs.execute(distinct_ID)
    # 출력
    print('문제 4번')
    print('-'*50,'\nUserID    UserName    addr\n', '-'*50, sep='')
    rows = curs.fetchall()
    for row in rows:
        print(row)
    # 종료
    conn.close()


# 5) 쇼핑몰 회원 중 주소가 경북과 경남인 회원 정보를 회원 아이디 순으로 출력
if  execute_num == 5:
    conn = ps.connect(host='localhost', user='root', password='1234', db='shoppingmall', charset='utf8')
    curs = conn.cursor()
    #  sql 문 입력
    addr_sort = """
    select ut.userID, userName, addr, 
        concat(mobile1, mobile2) as 연락처
    from user_table as ut
	    inner join buy_table as bt
	    on bt.userID = ut.userID 
    where addr in ('경북', '경남')
    order by userID """
    #   sql 문 실행
    curs.execute(addr_sort)
    #  출력
    print('문제 5번')
    print('-'*50,'\nUserID    UserName    addr      연락처\n', '-'*50, sep='')
    rows = curs.fetchall()
    for row in rows:
        print(row)
    #  종료
    conn.close()



# """
# ('KHD', '강호동', 1970, '경북', '011', '22222222', 182, '2007-07-07'),
# ('KJD', '김제동', 1974, '경남', NULL, NULL, 173, '2013-03-03'),
# ('KKJ', '김국진', 1965, '서울', '019', '33333333', 171, '2009-09-09'),
# ('KYM', '김용만', 1967, '서울', '010', '44444444', 177, '2015-05-05'),
# ('LHJ', '이휘재', 1972, '경기', '011', '88888888', 180, '2006-04-04'),
# ('LKK', '이경규', 1960, '경남', '018', '99999999', 170, '2004-12-12'),
# ('NHS', '남희석', 1971, '충남', '016', '66666666', 180, '2017-04-04'),
# ('PSH', '박수홍', 1970, '서울', '010', '00000000', 183, '2012-05-05'),
# ('SDY', '신동엽', 1971, '경기', NULL, NULL, 176, '2008-10-10'),
# ('YJS', '유재석', 1972, '서울', '010', '11111111', 178, '2008-08-08');
#
# (1, 'KHD', '운동화', NULL, 30, 2),
# (2, 'KHD', '노트북', '전자', 1000, 1),
# (3, 'KYM', '모니터', '전자', 200, 1),
# (4, 'PSH', '모니터', '전자', 200, 5),
# (5, 'KHD', '청바지', '의류', 50, 3),
# (6, 'PSH', '메모리', '전자', 80, 10),
# (7, 'KJD', '책', '서적', 15, 5),
# (8, 'LHJ', '책', '서적', 15, 2),
# (9, 'LHJ', '청바지', '의류', 50, 1),
# (10, 'PSH', '운동화', NULL, 30, 2),
# (11, 'LHJ', '책', '서적', 15, 1),
# (12, 'PSH', '운동화', NULL, 30, 2)
# """