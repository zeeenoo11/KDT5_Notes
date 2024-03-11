# ----------------------------------------------------------
# 함수 기능 : 회원 가입 기능
# 함수 이름 : joinMember
# 매개 변수 : 이름, 전화번호, 아이디, 이메일, 취미, 주소, 생일 ...
#            -> 가변, 다양한 종류 => 키워드 파라미터 : **member
# 반환값 : '가입 완료되었습니다.' : message
# ----------------------------------------------------------
def joinMember(**member):
    # print(type(member))   # 입력 타입을 알기 위함 -> dict
    print('joinMember1: ', member)
    members_j1.update(member)

# func_calling -----------------------------------------------
members_j1 = {}
# 다양한 키나 값의 종류에도 다 실행된다.
joinMember(name='Hong', age=17, birth='20240105')
joinMember(id = 'Hong84', phone = ['010-1111-2222'], job = 'actor', blood='O')
print('members_j1 :',members_j1)




# 회원 각각의 정보 기록 (입력마다 다른 키에 저장)
def joinMember2(**member):        # 방법1
    # 멤버 저장소에 멤버 추가
    members_j2[f'M{len(members_j2)+1}'] = member   # member를 members에 저장
    # len(members+1) : 입력하는 멤버의 저장된 순서를 키로 입력함

def joinMember2_ver2(**member):   # 방법2
    membersList.append(member)        # 얘는 맴버가 리스트일때만 가능

def joinMember2_ver3(**member):   # 방법3
    for k,v in member.items():
        members_j2_3[k] = v

# 다양한 키나 값의 종류에도 다 실행된다.
members_j2 = {}
members_j2_3 = {}
membersList = []
joinMember2(name='Hong', age=17, birth='20240105')
joinMember2(id = 'Hong84', phone = ['010-1111-2222'], job = 'actor', blood='O')
print(members_j2) # 출력 성공! 앞 members와 곂쳤기 때문
print(members_j2_3)
print(membersList)




# 필수 요소가 포함된 함수
# --------------------------------------------------------------
# 함수 기능 : 회원 가입 기능; 필수 요소를 포함함
# 함수 이름 : joinMember3
# 매개 변수 : 필수 => id, pw
#             선택 => **option 이름, 전화번호, 이메일, ....
#             가변 + 데이터 정보 함께
# 반 환 값 : '가입이 완료되었습니다.' str
# --------------------------------------------------------------
def joinMember3(id, pw, **option):
    print('OK')  # id, pw 가 있어야만 OK 출력

# joinMember3(name='Hong', age=17, birth='20240105')  # => 오류 발생
joinMember3(id = 'Hong84', pw = '1234', phone = ['010-1111-2222'], job = 'actor', blood='O')

# {키=값} 형식이 아니면 순서대로 id, pw 를 지정하게 됨
joinMember3(12, 34)      # OK




# 기본값(defalt) 설정
# --------------------------------------------------------------
# 함수 기능 : 회원 가입 기능; 필수 요소를 포함; 기본값 설정
# 함수 이름 : joinMember4
# 매개 변수 : 필수 => id, pw, loc, gender
#             선택 => **option 이름, 전화번호, 이메일, ....
#             가변 + 데이터 정보 함께
# 반 환 값 : '가입이 완료되었습니다.' str
# --------------------------------------------------------------
def joinMember4(id, pw, loc='내국인', gender='남자', **option):
    print(id, pw, loc, gender, option)  # loc, gender 자동 입력됨

# joinMember4(name='Hong', age=17, birth='20240105')  # => 오류 발생
joinMember4(id = 'Hong84', pw = '1234', phone = ['010-1111-2222'], job = 'actor', blood='O')
joinMember4(id = 'Hong84', pw = '1234', phone = ['010-1111-2222'], gender='여자', job = 'actor', blood='O')


# 아직 *data와 **datas의 차이를 잘 모르겠음 -> 교재 392p
# ** 는 데이터의 쌍을 가져오라는 뜻이다!


# => dict(키=값 데이터) 기준 : *data    -> 하나의 데이터만 가져옴 (키)
#                              **datas  -> 키=값 쌍을 가져옴



# 교재 387p ~
# 29 30장만 과제, 주말에 22~26장, 문제는 다 하고 시간 나면