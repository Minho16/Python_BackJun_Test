# first mode through functions

def calculate(first_num, second_num, operator):
    if operator == "add":
        return first_num + second_num
    elif operator == "subtract": 
        return first_num - second_num
    elif operator == "multiplication": 
        return first_num * second_num 
    elif operator == "division":
        return first_num / second_num 
    else:
        print("Please check your input") 
            
print(calculate(10,2,operator="add"))


# second mode through inputs

mode = input('Enter math operation(+,-,*,/): ')
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number: '))

if mode == '+':
    print(f'Answer is: {num1 + num2}')
elif mode == '-':
    print(f'Answer is: {num1 - num2}')
elif mode == '*':
    print(f'Answer is: {num1 * num2}')
elif mode == '/':
    print(f'Answer is: {num1 / num2}')
else:
    print('Input error!')