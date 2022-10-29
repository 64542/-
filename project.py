'''#count()
print('hello world'.count('l')>0)
'''
'''#in
print('a' in 'apple')

email = 'fuck@fuck.com'
print('@' in email)
'''
'''#문자열의 특정 부분만 가져올 수 있다.
s = 'hello'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

for i in range(5):
    print(s[i])
양수인덱스  [0123456]
            [abcdefg]
음수인덱스  [-7-6-5-4-3-2-1]
'''
'''#index()
#문자열에 특정 글자가 어디에 있는가?
s='zoo'
if 'g' in s:
    print(s.index('g'))
print('haha')
'''
'''#부분 문자열
#[start : end index : skip? jump?]
#[시작 : 끝 : 계단]

s = '010-9882-9831'
#9882
print(s[4:8])
#문자열 뒤집기
print(s[::-1])
'''
'''#문자열 치환
#replace('A','B')

s='123456789'
print(s.replace('3','짝'))

for i in range(1, len(s)+1):
    if i % 3 == 0:
        print(s.replace(str(i),'짝'))

s = '010-9882-9831
print(s.replace('-',''))
'''
'''#대 소 문자 변환
#lower(소문자로 변환),upper(대문자로 변환)
s='AbCdEfG'
print(s)
print(s.lower())
print(s.upper())

#계정 가입시 대소문자를 구별하지 않을때
new_account = 'AbCdEfG'
old_account = 'ABCDEFG'

print(new_account.lower()==old_account.lower())
print(old_account.upper()==new_account.upper())
'''
'''#f string
#print(f'이 안에서 포맷팅이 이루어 진다.') 변수는 {} 안에 적는다
n = 365
w = 7
print(f'일 년은 {n}일 이고 일주일은 {w}일 이다.')
#소숫점 자리를 프린트 문에서 처리 가능
pi = 3.141592
print(f'{pi:.4f}')
'''
'''#2진수와 8진수와 16진수로 나타내기 b=2진수 o=8진수 x=16진수
x = 314
print(f'{x:b}')
print(f'{x:o}')
print(f'{x:x}')
'''
'''#별 출력
print('*'*1)
print('*'*2)
print('*'*3)
print('*'*2)
print('*'*1)
'''
'''#소수 일정자리 이후 제거
pi = 3.14159265358979323846264338327
print(int(pi*100)/100)
print(int(pi*1000000)/1000000)
'''
'''#조건문은 어떤 특정한 상황에서 코드를 실행하거나, 실행하지 않는 방법을 코딩하는 방법입니다.
#온도
temperature = 31
#일정 온도 이상일때 실행하는 조건문
if temperature >= 30:
    print('ice cream')

if True:
    print('A')
if False:
    print('B')

if int(input())%2==0:
    print('짝수')
else :
    print('홀수')

if None :
    if None :
        if None :
            if None :
#if hell에 빠지지 않게 조심

#bmi 구하기
h = None / 100
w = None
i = w/(h * h)
if i >= 25 :
    print('비만')
elif i>= 23 and i < 25 :
    print('과체중')
elif i >= 18.5 and i < 23 :
    print('정상')
else :
    print('저체중')
'''
'''#loop 문 즉 반복문
#while 과 for
#보통 for 문을 많이 쓰지만 while문을 쓸때 더 깔끔하게 떨어지는 경우가 있다.
#둘다 반복을 하는것은 비슷하나 초기 조건을 거는 법, 루프를 빠져나오는 방법이 다르다.
for i in range(2,7,2):
    print(i)

#break continue
for i in range(5):
    n = int(input())
    if n == 0:
        print(f'{i}번 불량')
        continue
    print(f'{i}번 정상')

#찬성표와 반대표를 받아서 다수결을 판별하여 누가 이겼는지 출력
ok = 0
no = 0
for i in range(10):
    n = str(input())
    if n == '찬성':
            ok+=1
    elif n == '반대':
            no+=1
    else :
            print('기권표')
if ok > no:
    print('찬성')
elif ok < no:
    print('반대')
else:
    print('무효')

#조건이 있는데 그게 끝나는 범위가 정해져 있지 않은 경우 while문이 좋음
while True:
    n = int(input())
    if n == 9999:
        break
    else:
        print(n)
#pass None은 비운상태로 두기 pass는 그냥 넘기기
while True:
    pass
#비밀번호 설정후 입력하기
password = 5642
while True:
    n = int(input())
    if n == password :
        print('어서오고')
        break
    else :
        print('누구냐 넌')
'''
'''#함수
#코딩을 빠르게 하려면 타이핑을 줄여야 한다.
#타이핑된 내용이 간단해지면 메모리 사용량또한 감소하기 때문
#이미 쳤던 부분을 다시 치지 않게 함수를 사용한다.

#함수는 '입력인수'와 '출력값' 과 '계산' 이 핵심이다.

def add(a, b):
    r = (a * b)/2
    return r

print(int(add(1, 2)))

def func1(x):
    return x + 1
def func2(x):
    return x * 2
def func3(x):
    return x**3

print(func3(func2(func1(1))))

def Countdown(n):
    if n == 0:
        return
    print(n)
    Countdown(n-1)
Countdown(10)

def my_func(a):
    pass
print(my_func(1))

'''
'''#함수 해설
def 함수이름(인수 리스트):
    함수에 종속된 하위실행코드
    return 리턴값
    리턴키워드
print(함수이름(인수))
'''
'''#clss함수
#.(dot) replace(), append(), split()
#clss함수는 dot뒤에 붙이는 함수
'''



