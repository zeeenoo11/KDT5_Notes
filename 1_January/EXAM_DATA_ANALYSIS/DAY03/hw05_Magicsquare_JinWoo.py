# [ 과제2 ] 마방진 그리기
# 홀수를 입력 받고 해당하는 n x n 형태의 마방진을 구현하시오
# - 짝수 입력 시 오류 출력
# - n x n 이차원 배열 생성: 3 5 7 9
# - 자리수 맞춤

def get_frame_size():
    '''
    입력값이 홀수인지 판별하는 함수
    :return: int(frame_size)
    '''
    while True:  # 홀수 정수를 입력 받으면 종료
        f_size = input('홀수차 배열의 크기를 입력하세요: ')
        if f_size.isdecimal():  # 입력값이 숫자라면
            if int(f_size) % 2: # 짝수는 0 :False
                break
            else: print('Please Type Odd Number.')
        else: print('Only number approved.')
    return int(f_size)


def make_magic_square(n):
    '''
    마방진 제작 및 출력 함수
    :param n: 마방진 한 줄의 크기
    :return: None
    '''
    frame = [[0 for _ in range(n)] for _ in range(n)]  # 전체 틀 생성
    x = n//2; y = 0  # 중간열, 첫행에 첫번째 값 입력
    for i in range(n**2):       # 모든 인덱스: n^2 개
        frame[y][x] = 1 + i     # 1, 2, 3, ... 입력
        if frame[(y-1)%n][(x+1)%n]:  # 오른쪽 위 인덱스가 0이 아니라면
            y = (y+1) % n       # 아래 인덱스에 추가
        else:                   # 0이라면 오른쪽 위 인덱스에 추가
            x = (x + 1) % n
            y = (y - 1) % n

    print(f'Magic Square ({n} x {n})')
    for row in range(n):  # 마방진 출력문
        for col in range(n):
            print(f'{frame[row][col]:2d}', end=' ')
        print()


frame_size = get_frame_size()
make_magic_square(frame_size)