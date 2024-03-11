import pymysql
import pandas as pd


examples = 6  # 실행할  예제 번호
# ========= <MySQL과 Python 연동하기> ======================

if examples == 1:
    '''
    MySQL 와 Python 연동하기
    '''
    # database 연결
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='sakila', charset='utf8')

    # 커서 생성
    cur = conn.cursor()

    #  쿼리 실행
    cur.execute('select * from language')

    #  결과 가져오기
    rows = cur.fetchall()   # 모든 데이터를 가져옴
    print(rows)
    language_df = pd.DataFrame(rows)   # DataFrame 형태로 변환
    print(language_df)

    # 커서 종료, 연결 종료
    cur.close()
    conn.close()


if examples == 2:
    '''
    [ inner join ]
    '''
    # database 연결
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='sakila', charset='utf8')

    # 커서 생성
    cur = conn.cursor()

    query = """
    select c.email
    from customer as c
        inner join rental as r
        on c.customer_id = r.customer_id
    where date(r.rental_date) = (%s)"""
    # %s :  쿼리 실행시 값을 채워 넣을 자리

    #  쿼리 실행
    cur.execute(query, '2005-06-14')

    #  결과 가져오기
    rows = cur.fetchall()   # 모든 데이터를 가져옴
    for row in rows:
        print(row)

    # 커서 종료, 연결 종료
    cur.close()
    conn.close()

if examples == 3:
    '''
    [ try, except: 예외처리 ]
    '''
    def create_table(conn, cur):
        try:
            query ="""
                     create table customer2
                     (name varchar(10),
                     category smallint,
                     region varchar(10)
                     )"""

            cur.execute(query)
            conn.commit()
            print('Table created')

        except Exception as e:
            print(e)


    def main():
        # 데이터베이스(sqlclass_db) 연결
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='sqlclass_db', charset='utf8')

        # 커서 생성
        cur = conn.cursor()

        # 테이블 생성
        create_table(conn, cur)

        # 커서 종료, 연결 종료
        cur.close()
        conn.close()
        print('Database 연결 종료')

    main()

if examples == 4:
    '''
    execute() 예제
    '''
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='sqlclass_db', charset='utf8')

    curs = conn.cursor()
    sql = """insert into customer2(name, category, region) 
    values (%s, %s, %s)"""

    curs.execute(sql, ('홍길동', 1, '서울'))
    curs.execute(sql, ('박히진', 2, '서울'))

    conn.commit()
    print('Insert 완료')

    curs.close()
    conn.close()

if examples == 5:
    '''
    여러 개의 튜플 데이터 입력
    '''
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='sqlclass_db', charset='utf8')

    curs =  conn.cursor()
    sql = """Insert into customer2(name, category, region)
    values (%s, %s, %s)"""
    data = (
        ('홍진우', 1, '서울'),
        ('박지성', 2, '부산'),
        ('김연아', 3, '경기')
        )

    curs.executemany(sql, data)

    conn.commit()
    print('executemany 완료')
    curs.close()
    conn.close()

if examples == 6:
    '''
    Update, Delete
    '''
    conn = pymysql.connect(host='localhost', user='root', password='1234', db='sqlclass_db', charset='utf8')

    curs = conn.cursor()
    sql = """Update customer2
             set region = '서울특별시'
             where region = '서울'"""
    curs.execute(sql)
    print('Update 완료')

    sql = "Delete from customer2 where name = %s"
    curs.execute(sql, '홍길동')
    print('Delete 홍길동')

    conn.commit()
    curs.close()
    conn.close()

# FIN.