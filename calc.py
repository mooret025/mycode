#!/usr/bin/env python3
  
class Calculator:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y



def main():
    while True:
        num1 = input('Enter a number or "q" to quit: ')
        if num1 == 'q':
            break
        num2 = input('Enter another number: ')
        
        choice = input("""
Choose the operation you want to perform:
1. add
2. subtract
3. multiply
4. divide
>> """)

        calc = Calculator(num1, num2)
        if choice == '1':
            print(f'{num1} + {num2} is {calc.add()}')
        elif choice == '2':
            print(f'{num1} - {num2} is {calc.subtract()}')
        elif choice == '3':
            print(f'{num1} * {num2} is {calc.multiply()}')
        elif choice == '4':
            try:
                print(f'{num1} / {num2} is {calc.divide()}')
            except ZeroDivisionError:
                print('You attempted to divide by zero')
            finally:
                main()

main()
