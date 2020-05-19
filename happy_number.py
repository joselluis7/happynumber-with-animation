def happy_number(num):
    sum = rem = 0
    while num > 0:
        rest = num%10
        sum += rest**2
        num=num//10
    return sum

num = int(input("Introduce the number: "))
while( happy_number(num) != 1 and happy_number(num) != 4):
    num = happy_number(num)

if num == 1:
    print("happy number")
else:
    print("This is not a happy number")
