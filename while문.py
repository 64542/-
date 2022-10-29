
while True:         #계속 돌아라
    print(1)        #1을 출력하라


n = int(input())                        #while문의 범위를 받는다
i = 1                                   #약수를 정할 변수지정
count = 0                               #약수의 갯수를 샐 방을 만듬
while i < n+1:                          #약수의 범위에 포함이 된다면 반복하라
    if n % i == 0:                      #약수인지 구함
        count += 1                      #약수의 갯수를 추가
        print(f'{i}는 {n}의 약수')       #약수를 추가
    i += 1                              #약수를 정할 변수를 증가
print(f'{n}의 약수의 갯수는 {count}개')   #약수의 갯수를 출력
