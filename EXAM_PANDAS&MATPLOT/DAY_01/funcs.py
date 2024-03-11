def add(x,y): return x+y

def div(x,y): return x/y if y else None

# import할 모듈에 출력문/리턴값이 있는 경우:
#  -
print(f'funcs.py => __name__ : {__name__}')
print(f'add(3,4):',add(3,4))
print(f'div(3,4):',div(3,4))
