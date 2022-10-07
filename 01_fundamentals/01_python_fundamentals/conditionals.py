num = 20
if num > 40:
    print('greater than 40')
elif num > 30:
    print('greater than 30')
else:
    print('not greater than 40 or 30')

for i in range(1, 101):
    if i % 3 ==0 and i % 5 ==0:
        print("fizz_buzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)

