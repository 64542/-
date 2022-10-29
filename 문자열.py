s = 'sungil high-school'    #변수s에 문자열을 넣음
count = 0                   #갯수를 샐 변수 지정
for c in s:                 #c가 s라는 변수의 안에 있다면 반복한다
    if c == 's':            #만약에 c가 s안에 있다면 
        count += 1          #count를 1 증가시킨다
print(count)                #count를 출력한다

s = 'abcdefg'               #변수 s에 문자열을 넣는다
print(s[1:3])               #변수 s에 있는 문자열에서 1번을 출력하고(여기선 a가 0임) 3번을 출력(여기선 a가 1임)
print(s[0:8:2])             #변수 s에 있는 문자열에서 0번부터 8번까지 2개씩 건너뛰면서 출력함

s = 'abc'
sr = s[::-1]
print(sr)

s = 'Jello'
s = s.replace('J', 'H')
print(s)

s = '01245'
s = s[0:3] + '3' + s[3:]
print(s)