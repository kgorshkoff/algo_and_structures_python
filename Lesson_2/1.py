"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

while True:
    oper = input("Выберите действие (+, -, *, /) или 0 для завершения программы: ")
    if oper == '0': break
    if oper in '+-*/':
        x = float(input("Первое число = "))
        y = float(input("Второе число = "))
        if oper == '+':
            print(x + y)
        elif oper == '-':
            print(x - y)
        elif oper == '*':
            print(x * y)
        elif oper == '/':
            if y != 0:
                print(x / y)
            else:
                print("На ноль делить нельзя!")
    else:
        print("Неверный знак операции!")
