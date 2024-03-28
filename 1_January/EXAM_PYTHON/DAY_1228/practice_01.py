# [실습1]
# 1.1. 숫자 입력
number1 = float(input('숫자를 입력하세요: '))
number2 = float(input('두 번째 숫자를 입력하세요: '))
# 1.2. 출력
print(f'{number1} +  {number2} = {number1+number2:.1f}')
print(f'{number1} -  {number2} = {number1-number2:.1f}')
print(f'{number1} /  {number2} = {number1/number2:.1f}')
print(f'{number1} *  {number2} = {number1*number2:.1f}')
print(f'{number1} // {number2} = {number1//number2:.1f}')
print(f'{number1} %  {number2} = {number1%number2:.1f}')
print(f'{number1} ** {number2} = {number1**number2:.1f}')

# [실습2]
# 2.1. 비교 연산
print(f'{number1} >  {number2}\t => {number1>number2}')
print(f'{number1} <  {number2}\t => {number1<number2}')
print(f'{number1} >= {number2}\t => {number1>=number2}')
print(f'{number1} <= {number2}\t => {number1<=number2}')
print(f'{number1} == {number2}\t => {number1==number2}')
print(f'{number1} != {number2}\t => {number1!=number2}')

# [실습3]
# - 최대값과 최소값을 추가로 입력 받고 논리 연산 결과 출력
# 3.1.
maximum = float(input('최대값을 입력: '))
minimum = float(input('최소값을 입력: '))

# 3.2. 출력
print(f'{number1}>{number2} and {number1}>{maximum}  => {number1>number2 and number1>maximum}')
print(f'{number1}>{number2} and {number1}>{minimum}  => {number1>number2 and number1>minimum}')
print(f'not {number1}    => {not number1}')

