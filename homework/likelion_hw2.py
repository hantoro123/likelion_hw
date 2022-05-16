## 과제 1번

def plus(x,y):     # x, y를 더하는 함수
    return x+y

def minus(x,y):    # x, y를 빼는 함수
    return x-y

def multiply(x,y): # x, y를 곱하는 함수
    return x*y

def division(x,y): # x, y를 나누는 함수
    return x/y

while True:      # 무한 반복
    # split()을 통해 공백을 기준으로 문자를 받고 map으로 두 변수를 동시에 int형으로 받는다.
    a,b = map(int,input('연산을 진행할 두 숫자를 입력하시오 : ').split())
    oper = input('어떠한 연산을 수행할까요?')
    # 각 연산자를 비교하며 알맞는 함수를 콜한다.
    if oper == '+':
        print(f'{a} + {b} = {plus(a,b)}\n')
    elif oper == '-':
        print(f'{a} - {b} = {minus(a,b)}\n')
    elif oper == '*':
        print(f'{a} * {b} = {multiply(a,b)}\n')
    elif oper == '/':
        print(f'{a} / {b} = {division(a,b)}\n')
    else:
        print('해당 연산은 지원하지 않습니다.\n')

## 과제 2번

import random           # 난수를 추출하는 모튤
from time import sleep  # 원하는 만큼 기다리는 모튤

def lotto():            # 로또 함수
    print('번호 추출중...')
    win = random.sample(range(1,46),6) # 1~46까지 6개의 난수를 중복없이 추출
    win.sort() # 추출한 난수를 오름차순으로 정렬
    for i in range(1,6):
        print(f'{i} ...')
        sleep(1)            # 1s 쉰다.
    print('로또 번호는!!')
    print(f'{win} 입니다.')
    
    return 

if input() == 'y':
    lotto()
else:     # y가 아닌 값이 들어오면 종료
    print('로또 번호 추출을 종료합니다.')
