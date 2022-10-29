n = input() #기본 입력 받기
n = int(input()) #입력 받아서 정수형으로 바꾸기
n = input().split() #입력 받아서 쪼개기

a = int(n[0]) 
b = int(n[1]) #입력 받아서 int로 2개 받기
print(a+b)

n = input().split("*") #입력 받을때 쪼개는 기준을 *로 바꾸기
n = list(map(int,input().split())) #입력 받아서 쪼갠후 정수로 바꾸기