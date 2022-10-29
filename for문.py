
for i in range(1, 10, 2):       #1은 초기값, 10은 목표값, 2는 증가값
    print(i)                    #i안에 있는 값을 출력


n = int(input())                #약수의 범위를 받아옴
count = 0                       #약수의 갯수를 넣을 방을 만듬
for i in range(1, n+1):         #1부터 약수의 범위까지 돌아라
    if n % i == 0:              #만약에 약수라면
        print(i, end=',')       #약수를 출력하라(end=','를 붙이면 ,로 나눠서 한줄로 출력됨)
        count += 1              #약수의 갯수를 증가
print(count)                    #약수의 갯수를 출력
