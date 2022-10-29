from turtle import left


num = list(map(int, input().split()))
type = 0

for i in num :
    if i > 10000 or i < 1 :
        print("입력 오류")
        type = 1
    else :
        None

if type == 0 :
    f = num[0] * num[3]
    f1 = num[2] * num[1]
    mom = num[1] * num[3]
    son = f - f1

    left = 2
    while True :
        if mom % left !=0 and son % 2 != 0:
                break
        elif mom % left == 0 and son % left == 0:
            mom //= left
            son //= left
        else :
            left += 1
    print(f'{son}/{mom}')

else :
    None