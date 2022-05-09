## 1번 for문 이용 허들을 5번 넘는 코드를 작성

Hurdle = 0                   # 허들값을 0으로 초기화
for i in range(1,6):         # 1~5까지 1씩 커진다.
    Hurdle = i               # i가 1씩 커진게 Hurdle에 입력됨
    print("허들을 넘었습니다.")
    if Hurdle == 5:          # Huldle이 5가되면 실행문 실행
        print('레이스를 완주했습니다.')

# 2번 while문 이용 허들을 5번 넘고 허들의 개수를 나타내는 코드 작성

Hurdle = 5                      # 처음 허들 갯수 5개로 초기화
while Hurdle > 0:               # 허들이 0보다 클 때 반복
    print(f'허들이 {Hurdle}개 남았습니다.')
    Hurdle -= 1                 # 반복할 때 마다 허들 갯수 -1
print('레이스를 완주했습니다.')

## 3번 if문 사용 이름과 점수를 입력하여 학점을 나타내는 코드 작성

name = input()                     # 이름 입력
score = int(input())               # 점수를 정수형으로 입력

if score >= 90:                    # 90점 이상이면 A
    print(f'{name}의 학점 : A')
elif score in range(80,90):        # 80~89점 이면 B 
    print(f'{name}의 학점 : B')   
elif score in range(70,80):        # 70~79점 이면 C
    print(f'{name}의 학점 : C')
elif score in range(60,70):        # 60~69점 이면 D
    print(f'{name}의 학점 : D')
else:                              # 59점 이하면 B
    print(f'{name}의 학점 : F')

## 4번 for문 & if문 4명의 학생의 이름과 점수를 받고 학점 출력

for _ in range(4):                 # 3번을 4회 반복
    name = input()
    score = int(input())

    if score >= 90:
        print(f'{name}의 학점 : A')
    elif score in range(80,90):
        print(f'{name}의 학점 : B')
    elif score in range(70,80):
        print(f'{name}의 학점 : C')
    elif score in range(60,70):
        print(f'{name}의 학점 : D')
    else:
        print(f'{name}의 학점 : F')