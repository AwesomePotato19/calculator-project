# VARIABLES
total = 0
i = 0
num = []
op = []
n = 0
output = ''

def calc(a, b):
    if op[n] == "+":
        return a+b
    elif op[n] == "-":
        return  a-b
    elif op[n] == "x" or op[n] == '*':
        return a*b
    else:
        try:
            return a/b
        except ZeroDivisionError:
            print('Cannot divide by 0')

while True:

    if i%2 == 0:
        try:
            num.append(int(input("Enter number: ")))
        except ValueError:
            print('INVALID VALUE')
            continue 

    else:
        operator = input("Enter operator: ")
        if operator == '=':
            break
        elif operator in ['+', '-', '*', 'x', '/']:
            op.append(operator)
        else:
            print('INVALID OPERATOR!')
            continue
    i += 1

while n < len(op):
    if n == 0:
        total = calc(num[n], num[n+1])
        output += str(num[n])
    else:
        total = calc(total, num[n+1])
    
    output += ' ' + str(op[n]) + ' ' + str(num[n+1])
    n += 1

print(f'{output} \n= {total}')