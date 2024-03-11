import funcs as f

print(f'__name__ : {__name__}')

# funcs.py => __name__ : funcs           # import 되었다면 __name__=가져온 모듈명이다
# add(3,4): 7
# div(3,4): 0.75
# 0.4444444444444444 __name__ : __main__ # 해당 파일 내에선 main으로 나옴

if __name__ == '__main__':  # import된 함수, 명령이 작동X 하기 위함
    print(f.add(1,2))