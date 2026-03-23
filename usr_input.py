num1 = int(input("Enter a digit: "))
num2 = int(input("Enter a digit: "))

add_num = num1 + num2

if num1 % 2 == 0 and num2 % 2 == 0:
    print(add_num)
else:
    print("Only accepts even number.")
